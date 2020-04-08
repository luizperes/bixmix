# bixmix
> A collection of scripts that I use in the Parabix project

## Scripts:
- `multiple_llvm_flags`: Given a build folder with multiple LLVM versions (`-b` flag), a file with a set of flags separated by newline (`-c` flag), a regular expression (`-x` flag), a file with the folders where which LLVM version has been installed (`-l` flag) and a file target (`-t` flag), this script computes multiple combinations of the flag set and performs runtime comparisons using `perf`.

- `generate_dbs`: Creates databases for both PostgresSQL and SQLite3. In each databases, 5 tables are created in the format { `id`, `column` } and 100000 records are inserted at random
