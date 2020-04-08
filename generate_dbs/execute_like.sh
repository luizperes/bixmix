echo "SQLite '%(a_c_de_b_fe_%'"

time ./sqlite/sqlite3 ./sqlite/j "SELECT * FROM TB1 WHERE description LIKE '%a_c_de_b_fe_%'" > jaca
time ./sqlite/sqlite3 ./sqlite/j "SELECT * FROM TB2 WHERE description LIKE '%a_c_de_b_fe_%'" > jaca
time ./sqlite/sqlite3 ./sqlite/j "SELECT * FROM TB3 WHERE description LIKE '%a_c_de_b_fe_%'" > jaca
time ./sqlite/sqlite3 ./sqlite/j "SELECT * FROM TB4 WHERE description LIKE '%a_c_de_b_fe_%'" > jaca
time ./sqlite/sqlite3 ./sqlite/j "SELECT * FROM TB5 WHERE description LIKE '%a_c_de_b_fe_%'" > jaca


echo "Postgres '%(a_c_de_b_fe_%'"

time psql -d j -c "SELECT * FROM TB1 WHERE description LIKE '%a_c_de_b_fe_%'" --csv -o jaca
time psql -d j -c "SELECT * FROM TB2 WHERE description LIKE '%a_c_de_b_fe_%'" --csv -o jaca
time psql -d j -c "SELECT * FROM TB3 WHERE description LIKE '%a_c_de_b_fe_%'" --csv -o jaca
time psql -d j -c "SELECT * FROM TB4 WHERE description LIKE '%a_c_de_b_fe_%'" --csv -o jaca
time psql -d j -c "SELECT * FROM TB5 WHERE description LIKE '%a_c_de_b_fe_%'" --csv -o jaca

echo "Parabix '.*.(a.c|c.de|b.f|e).*'"

time ~/Projects/parabix-devel/build/bin/icgrep ".*.(a.c|c.de|b.f|e).*" out/10en > /dev/null
time ~/Projects/parabix-devel/build/bin/icgrep ".*.(a.c|c.de|b.f|e).*" out/50en > /dev/null
time ~/Projects/parabix-devel/build/bin/icgrep ".*.(a.c|c.de|b.f|e).*" out/100en > /dev/null
time ~/Projects/parabix-devel/build/bin/icgrep ".*.(a.c|c.de|b.f|e).*" out/500en > /dev/null
time ~/Projects/parabix-devel/build/bin/icgrep ".*.(a.c|c.de|b.f|e).*" out/1000en > /dev/null
