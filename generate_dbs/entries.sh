

node scripts/make_file.js 100000 10 > scripts/out/10en
node scripts/make_file.js 100000 50 > scripts/out/50en
node scripts/make_file.js 100000 100 > scripts/out/100en
node scripts/make_file.js 100000 500 > scripts/out/500en
node scripts/make_file.js 100000 1000 > scripts/out/1000en

node scripts/sqlentries.js scripts/out/10en TB1 > scripts/out/10en.sql
node scripts/sqlentries.js scripts/out/50en TB2 > scripts/out/50en.sql
node scripts/sqlentries.js scripts/out/100en TB3 > scripts/out/100en.sql
node scripts/sqlentries.js scripts/out/500en TB4 > scripts/out/50en.sql
node scripts/sqlentries.js scripts/out/1000en TB5 > scripts/out/1000en.sql
