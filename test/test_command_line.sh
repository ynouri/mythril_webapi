#!/usr/bin/env bash

curl -H "Content-Type: application/json" -X POST -d '{"submission_type": "bytecode", "bytecode": "0x5050"}' http://localhost:8000/mythril/v1/analysis/
