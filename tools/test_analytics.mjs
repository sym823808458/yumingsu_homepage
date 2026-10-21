// Network-free regression checks for tab deduplication and real-count rendering.
import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import vm from 'node:vm';
import {webcrypto} from 'node:crypto';

const source = readFileSync(new URL('../assets/analytics.js', import.meta.url), 'utf8');
const names = ['surfacia','gbline','handle-candle','pka-ml-education','tpa-calculation','building-wind-screening'];
function fixture() {
  const saved = new Map(), events = new Set();
  const state = {clock: Date.now(), counts: Object.fromEntries(names.map(n => [n, 0])), calls: [], loseResponse: false, badTotal: false};
  const data = () => ({counts: {...state.counts}, total: Object.values(state.counts).reduce((a,b) => a+b, 0) + (state.badTotal ? 1 : 0), started_at:'2026-10-21T09:42:03Z'});
  async function render({slug='', zh=false, hostname='yumingsu.top', storageBlocked=false} = {}) {
    const nodes = [...(slug ? [slug] : names), ...(slug ? [] : ['total'])].map(name => ({
      textContent:'…', dataset:{visitCount:name}, hasAttribute: attr => attr==='data-visit-total' && name==='total'
    }));
    vm.runInNewContext(source, {
      document:{body:{dataset:{analyticsProvider:'cloudflare-d1',analyticsEndpoint:'https://stats.yumingsu.top',analyticsHosts:'yumingsu.top,www.yumingsu.top,sym823808458.github.io',analyticsSoftware:slug,analyticsMinutes:'30'}},documentElement:{lang:zh?'zh-CN':'en'},querySelectorAll:()=>nodes},
      location:{hostname}, crypto:webcrypto, Uint8Array, Intl, AbortSignal,
      Date:{now:()=>state.clock},
      sessionStorage:{getItem:key=>{if(storageBlocked)throw Error('blocked');return saved.get(key)||null;},setItem:(key,value)=>{if(storageBlocked)throw Error('blocked');saved.set(key,value);}},
      fetch:async (url,options) => {
        state.calls.push({url,options});
        if(options.method==='POST') {
          const body=JSON.parse(options.body);
          assert.deepEqual(Object.keys(body).sort(),['event_id','software']);
          assert.ok(names.includes(body.software));
          assert.match(body.event_id,/^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/);
          if(!events.has(body.event_id)){events.add(body.event_id);state.counts[body.software]++;}
          if(state.loseResponse){state.loseResponse=false;throw Error('response lost after commit');}
        }
        return {ok:true,json:async()=>data()};
      }
    });
    for(let i=0;i<8;i++)await new Promise(resolve=>setImmediate(resolve));
    return nodes;
  }
  return {state,render};
}

test('homepage reads six persisted counts and their total, without recording visits', async()=>{
  const {state,render}=fixture();state.counts.gbline=12;state.counts.surfacia=3;
  const nodes=await render();assert.equal(nodes[0].textContent,'3');assert.equal(nodes[1].textContent,'12');assert.equal(nodes[6].textContent,'15');
  assert.equal(state.calls.length,1);assert.ok(state.calls.every(c=>!c.options.method));
  assert.equal(state.calls[0].options.credentials,'omit');assert.equal(state.calls[0].options.referrerPolicy,'no-referrer');
});
test('refresh and Chinese switch reuse the same tab visit without additional writes',async()=>{
  const {state,render}=fixture();assert.equal((await render({slug:'gbline'}))[0].textContent,'1');
  await render({slug:'gbline'});await render({slug:'gbline',zh:true});
  assert.equal(state.counts.gbline,1);assert.equal(state.calls.filter(c=>c.options.method==='POST').length,1);
});
test('each software and each elapsed 30-minute window has a separate event',async()=>{
  const {state,render}=fixture();await render({slug:'gbline'});await render({slug:'surfacia'});
  state.clock+=30*60000;await render({slug:'gbline'});
  assert.equal(state.counts.gbline,2);assert.equal(state.counts.surfacia,1);
});
test('lost network response retries the same event ID instead of incrementing twice',async()=>{
  const {state,render}=fixture();state.loseResponse=true;
  assert.equal((await render({slug:'tpa-calculation'}))[0].textContent,'1');
  await render({slug:'tpa-calculation'});
  const posts=state.calls.filter(c=>c.options.method==='POST');assert.equal(posts.length,2);
  assert.equal(JSON.parse(posts[0].options.body).event_id,JSON.parse(posts[1].options.body).event_id);
  assert.equal(state.counts['tpa-calculation'],1);
});
test('inconsistent data shows unavailable instead of invented totals or zeroes',async()=>{
  const {state,render}=fixture();state.badTotal=true;
  assert.ok((await render({zh:true})).every(n=>n.textContent==='暂时无法读取'));
});
test('local previews and unknown/hidden software do not call the service',async()=>{
  const {state,render}=fixture();await render({hostname:'localhost'});await render({slug:'multiwfn-ml-helper'});
  assert.equal(state.calls.length,0);
});
test('blocked session storage reads counts without generating undeduplicated visits',async()=>{
  const {state,render}=fixture();state.counts.surfacia=7;
  assert.equal((await render({slug:'surfacia',storageBlocked:true}))[0].textContent,'7');
  assert.equal(state.calls.filter(c=>c.options.method==='POST').length,0);
});
