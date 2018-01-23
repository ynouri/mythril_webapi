#!/usr/bin/env bash

# Posts a dummy bytecode submission and fetchs json result
curl -H "Content-Type: application/json" -X POST -d '{"submission_type": "bytecode", "bytecode": "0x5050"}' http://localhost:8000/mythril/v1/analysis/
