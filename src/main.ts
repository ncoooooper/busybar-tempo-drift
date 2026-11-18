import {desk} from "@shared/desk";
import {wrap} from "@shared/surface";
type S={taps:number[];page:number};const names=["Tempo","Early","Late","Drift"];
function bpm(a:number[]){return a.length?60000*a.length/a.reduce((s,v)=>s+v,0):0;}
desk<S>({name:"Tempo Drift",accent:"#6DA9E9",motion:{"motif":"interval","color":"#6DA9E9","shine":"#E2F4FF"},initial:()=>({taps:[],page:0}),render:s=>{
 const intervals=s.taps.slice(1).map((t,i)=>t-s.taps[i]),half=Math.floor(intervals.length/2);
 const overall=bpm(intervals),early=bpm(intervals.slice(0,half)),late=bpm(half?intervals.slice(-half):[]);
 const drift=late-early,valid=s.page===0?intervals.length>=1:intervals.length>=4;
 return {title:names[s.page],value:valid?(s.page===3&&drift>0?"+":"")+Math.round([overall,early,late,drift][s.page])+" BPM":"Tap beat",
 lines:["Taps "+s.taps.length+" / 24","Early "+Math.round(early)+" / late "+Math.round(late),"Delta "+(drift>0?"+":"")+drift.toFixed(1)+" BPM","Click: tap the beat","Wheel: compare halves","Start: new phrase"]};},
 action:(s,k,now)=>{if(k==="ok"){const last=s.taps[s.taps.length-1];if(last&&now-last<100)return;if(!last||now-last>4000)s.taps=[];s.taps=s.taps.concat([now]).slice(-24);}
 if(k==="start")s.taps=[];if(k==="up"||k==="down")s.page=wrap(s.page+(k==="up"?1:-1),4);}});
