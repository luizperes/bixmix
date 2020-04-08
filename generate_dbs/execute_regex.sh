
echo "Postgres '.*.(a.c|c.de|b.f|e).*'"

time psql -d j -c "SELECT * FROM TB1 WHERE description ~* '.*.(a.c|c.de|b.f|e).*'" --csv -o jaca
time psql -d j -c "SELECT * FROM TB2 WHERE description ~* '.*.(a.c|c.de|b.f|e).*'" --csv -o jaca
time psql -d j -c "SELECT * FROM TB3 WHERE description ~* '.*.(a.c|c.de|b.f|e).*'" --csv -o jaca
time psql -d j -c "SELECT * FROM TB4 WHERE description ~* '.*.(a.c|c.de|b.f|e).*'" --csv -o jaca
time psql -d j -c "SELECT * FROM TB5 WHERE description ~* '.*.(a.c|c.de|b.f|e).*'" --csv -o jaca

echo "Parabix '.*.(a.c|c.de|b.f|e).*'"

time ~/Projects/parabix-devel/build/bin/icgrep ".*.(a.c|c.de|b.f|e).*" out/10en > /dev/null
time ~/Projects/parabix-devel/build/bin/icgrep ".*.(a.c|c.de|b.f|e).*" out/50en > /dev/null
time ~/Projects/parabix-devel/build/bin/icgrep ".*.(a.c|c.de|b.f|e).*" out/100en > /dev/null
time ~/Projects/parabix-devel/build/bin/icgrep ".*.(a.c|c.de|b.f|e).*" out/500en > /dev/null
time ~/Projects/parabix-devel/build/bin/icgrep ".*.(a.c|c.de|b.f|e).*" out/1000en > /dev/null
