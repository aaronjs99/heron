#!/usr/bin/env bash
set -Eeuo pipefail

# This simple wrapper allowing us to pass a set of
# environment variables to be sourced prior to running
# another command. Used in the launch file for setting
# robot configurations prior to xacro.

ENVVARS_FILE="$1"
shift 1

set -a
# shellcheck disable=SC1090
source "$ENVVARS_FILE"
set +a

exec "$@"
