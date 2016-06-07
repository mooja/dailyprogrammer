#!/usr/bin/env node

// Daily Programmer Challenge 230 Easy

// https://www.reddit.com/r/dailyprogrammer/comments/3j3pvm/20150831_challenge_230_easy_json_treasure_hunt/

// 07 June 2016

const readline = require('readline');


// recursive version (breaks on big objects)
function get_path(obj, target) 
{
    switch (typeof obj) 
    {
        case 'list':
        case 'object':

            for (let key in obj) 
            {
                let path = get_path(obj[key], target);

                if (path === true) 
                    return key;

                if (typeof path === 'string')
                    return [key, path].join(' -> ');
            }
            break

        default:

            if (obj === target)
                return true;

            return false;
    }
}

// queue version
function get_path_queue(obj, target, breadth_first=true) {
    let queue = [{path: [], obj: obj}];

    while(queue)
    {
        let item = null;
        if (breadth_first)
            item = queue.shift();
        else
            item = queue.pop()

        if(item.obj === target)
            return item.path.join(' -> ');

        if(typeof item.obj === 'list') 
        {
            for (let i = 0; i < item.obj.length; i++) 
            {
                queue.push({
                    path: [...item.path, i],
                    obj: item.obj[i]
                })
            }
        }

        if(typeof item.obj === 'object') 
        {
            for (let key in item.obj) 
            {
                queue.push({
                    path: [...item.path, key],
                    obj: item.obj[key]
                })
            }
        }

    }

    return false;
}


const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let lines = [] 
rl.on('line', line => lines.push(line))
rl.on('close', () => {
    let json_string = lines.join('\n');
    let obj = JSON.parse(json_string);
    console.log(get_path(obj, 'dailyprogrammer'));
})
