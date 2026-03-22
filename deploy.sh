#!/usr/bin/env bash

if ! command -v hugo >/dev/null 2>&1; then
	echo "Error: 'hugo' is not installed or not on PATH." >&2
	exit 1
fi

if ! command -v async-neocities >/dev/null 2>&1; then
	echo "Error: 'async-neocities' is not installed or not on PATH." >&2
	exit 1
fi

hugo
async-neocities --cleanup
async-neocities --supporter