#!/usr/bin/env node

// Daily Programmer Challenge 211 Easy
 
// https://www.reddit.com/r/dailyprogrammer/comments/338p28/20150420_challenge_211_easy_the_name_game/

// 19 May 2016

class SimpleNameRhyme {
  constructor(name) {
    this.name = name;
  }

  rhyme() {
    let suffix = this.name.slice(1);
    let rhyme = `${this.name}, ${this.name} bo B${suffix}\n`;
    rhyme += `Bonana fanna fo F${suffix}\n`;
    rhyme += `Feel fy mo M${suffix}\n`;
    rhyme += `${this.name}!\n`;
    return rhyme;
  }
}

class AdvancedNameRhyme extends SimpleNameRhyme {
  rhyme() {
    let suffix = this.name.slice(1);
    let name_rhymes = [
      'B' + suffix,
      'F' + suffix,
      'M' + suffix
    ].map(name => {
      if (name[0] == this.name[0])
        return name[0].toLowerCase() + 'o-' + suffix;
      else if ('AEIOU'.indexOf(this.name[0]) != -1)
        return name[0] + this.name.toLowerCase();
      return name;
    });

    let rhyme = `${this.name}, ${this.name} bo ${name_rhymes[0]}\n`;
    rhyme += `Bonana fanna fo ${name_rhymes[1]}\n`;
    rhyme += `Feel fy mo ${name_rhymes[2]}\n`;
    rhyme += `${this.name}!\n`;
    return rhyme;
  }
}


lincoln_rhyme = new AdvancedNameRhyme('Lincoln');
mary_rhyme = new AdvancedNameRhyme('Mary');
arnold_rhyme = new AdvancedNameRhyme('Arnold');

console.log(lincoln_rhyme.rhyme());
console.log(mary_rhyme.rhyme())
console.log(arnold_rhyme.rhyme())
