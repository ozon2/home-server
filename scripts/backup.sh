#!/bin/bash
# Run in a tmux!

set -eu

. .env

export RESTIC_REPOSITORY RESTIC_PASSWORD

restic --exclude-file "exclude.txt" -v backup /

echo
echo "Backup done, cleaning up old backups..."
echo

restic forget --keep-daily 7 --keep-weekly 4 --keep-monthly 12 --keep-yearly 2

restic prune

echo
echo "Checking backups"
echo

restic check
