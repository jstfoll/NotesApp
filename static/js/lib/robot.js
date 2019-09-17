CodeMirror.defineSimpleMode("robot", {
    start: [
      {regex: /\*+\s*(settings?|metadata|(user )?keywords?|test ?cases?|variables?)/i, token: "section", sol:true},
      {regex: /\s*\[?Documentation\]?/i, token: "documentation", sol:true},
      {regex: /\[(Arguments|Setup|Teardown|Precondition|Postcondition|Template|Return|Timeout)\]/i, token: "tc_settings"},
      {regex: /0x[a-f\d]+|[-+]?(?:\.\d+|\d+\.?\d*)(?:e[-+]?\d+)?/i, token: "numeric"},
      {regex: /((?<!\\)|(?<=\\\\))[$@&%]\{.*\}/, token: "variable"},
      {regex: /(^| {2,}|	|\| {1,})(?<!\\)#.*$/, token: "comment"},
    //   {regex: /(^[^ \t\*\n\|]+)|((?<=^\|)\s+[^ \t\*\n\|]+)/, token: "meta", mode:{spec:"control", end:/(?=\s{2})|\t|$|\s+(?=\|)/}},
      {regex: /\s*(Login|Click|Enter|Exist|Navigate)/i, token: "keyword", sol:true},
      {regex: / {2}[\w-_/]+/i, token: "literal"}
    ],
    // The multi-line comment state.
    comment: [
      {regex: /.*?\*\//, token: "comment", next: "start"},
      {regex: /.*/, token: "comment"}
    ],
    meta: {
      dontIndentStates: ["comment"],
      lineComment: "#"
    }
  });