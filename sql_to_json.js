
var mysql      = require('mysql');
var fs = require('fs');

var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  database : 'igem'
});

connection.connect();

var parts = [];

connection.query('SELECT * FROM parts', function(err, rows, fields) {
  if (err) throw err;

  console.log(rows.length + ' rows');

  rows.forEach(function(row) {

      delete row.sequence_sha1;
      delete row.seq_edit_cache;

  });

  /*
  rows = rows.sort(function(a, b) {

      return a.part_id - b.part_id;

  });*/

  //console.log(JSON.stringify(rows[0]));
  //
  fs.writeFileSync('parts.json', JSON.stringify(rows, null, 2));
});

connection.query('SELECT * FROM parts_seq_features', function(err, rows, fields) {
  if (err) throw err;

  console.log(rows.length + ' rows');

  /*
  rows = rows.sort(function(a, b) {

      return a.part_id - b.part_id;

  });*/

  //console.log(JSON.stringify(rows[0]));
  //
  fs.writeFileSync('parts_seq_features.json', JSON.stringify(rows, null, 2));
});


connection.end();
