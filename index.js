/* 1. expressモジュールをロードし、インスタンス化してappに代入。*/
var express = require("express");
var app = express();
var execSync = require('child_process').execSync;

funcs = {
    "search" : function(keyword, ctype) {
        console.log("scraping start")
        var cmd = "python3 scrape.py --keyword " + keyword + " --ctype " + ctype
        var result = execSync(cmd);
        return result ;
    }
}

/* 2. listen()メソッドを実行して3000番ポートで待ち受け。*/
var server = app.listen(3000, function(){
    console.log("Node.js is listening to PORT:" + server.address().port);
});

/* 3. 以後、アプリケーション固有の処理 */

app.get('/:keyword/:ctype/', function (req, res) {
    console.log("got request")
    var keyword = req.params.keyword ;
    var ctype = req.params.ctype ;
    var msg = funcs["search"](keyword, ctype);
    res.send(msg + "\n");
  });
