---
title: Notes: Master of Regular Expression
author: Haisheng, Wu
tags: reading, regex
---

# Notes

~~~~~~{.perl}
Matching and Capture, or just not Capture
(?:...) and (...)


/i has no effect on the replacement text
e.g.  $var =~ s/\bJeff\b/Jeff/i;
compare difference with:
$var =~ s/\sJeff\s/Jeff/i;


Automated Editing
perl -p -i -e 's/sysread/read/g' file


? What is 'm' modifier
$text =~ s/^$/<p>/mg;

~~~~~~

~~~~~~{.perl}
Lookaround
  (?= ...) (?! ...) (?<= ...) (?<! ...)
  - lookaround does not consume text
  - (?=Jeffery)Jeff <P61>
  - (?<=\bJeff)(?=s\b)


\G <P128>
  X? ...

Comments and Mode modifiers <P133>
  (?modifier) such as (?i), (?-i)
  e.g. <B>(?i)very(?-i)</B>
       match: <B>VERY</B>
              <B>Very</B>
       but not: <b>Very</b>
  (?modifier:), (?i: ...)


Named Capture <P137>
Atomic grouping
  (?> ...)

Class set opertions <P123>
  [[a-z]&&[^aeiou]]
  "this and not that"

Greedy quantifiers <P139>
Lazy (Non-Greedy) quantifiers

~~~~~~

~~~~~~{.perl}
quiz
where does fat|cat|belly|you match in the string
 "The dragging belly indicates your cat is too fat"

Apply ^.*([0-9]+) to "Copyright 2003",
 what's captured by parentheses?
~~~~~~

~~~~~~{.perl}
### "look around"
$test = "see Jeffs book";
$test =~ s/(?<=Jeff)(?=s)/'/g;
print "$test \n";    ### expect see Jeff's book

### Start of match ( or end of previous match): \G
$test = "abcde";
$test =~ s/\Gx?/!/g;
print "$test \n";             ### expect !abcde
$test =~ s/\x?/!/g;
print "$test \n";             ### expect !a!b!c!d!e

~~~~~~

# Reference
