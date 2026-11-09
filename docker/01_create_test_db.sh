#!/bin/sh
set -eu
# Apenas no primeiro arranque do volume PostgreSQL.
# Base exclusiva dos testes: a BD de demonstração fica intacta.
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" \
  -c 'CREATE DATABASE smartdesk_test;'
