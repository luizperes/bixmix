mkdir scripts/out

psql --file scripts/createdb -d j

./sqlite/sqlite3 sqlite/j -init ../scripts/createdb ""

bash scripts/entries.sh

psql --file scripts/out/10en.sql -d j
psql --file scripts/out/50en.sql -d j
psql --file scripts/out/100en.sql -d j
psql --file scripts/out/500en.sql -d j
psql --file scripts/out/1000en.sql -d j

./sqlite/sqlite3 sqlite/j -init scripts/out/10en.sql ""
./sqlite/sqlite3 sqlite/j -init scripts/out/50en.sql ""
./sqlite/sqlite3 sqlite/j -init scripts/out/100en.sql ""
./sqlite/sqlite3 sqlite/j -init scripts/out/500en.sql ""
./sqlite/sqlite3 sqlite/j -init scripts/out/1000en.sql ""
