#!/usr/bin/env node

// Daily Programmer Challenge 209 Easy
//
// https://www.reddit.com/r/dailyprogrammer/comments/31ls3h/20150406_challenge_209_easy_the_button_can_be/
//
// 17 May 2016

const raw_data = `UserA: 41.04
UserB: 7.06
UserC: 20.63
UserD: 54.28
UserE: 12.59
UserF: 31.17
UserG: 63.04`

let user_times = raw_data.split('\n').map(line => {
  let [user, time] = line.split(': ');
  let ut = {
    'user': user,
    'time': parseFloat(time)
  };
  return ut;
});
user_times.sort((a, b) => a.time - b.time);

let btn_times = [];
for (var i in user_times) {
  let ut = user_times[i];
  if (i == 0)
    var btime = 60 - ut.time;
  else
    var btime = (60 + btn_times[i - 1].time) - ut.time
  btn_times.push({
    user: ut.user,
    time: ut.time,
    btime: btime
  });
}

btn_times.forEach(bt => {
  let row = $(`${bt.user}: ${Math.floor(bt.btime)}`);
  console.log(row);
})
