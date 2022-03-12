#!/bin/bash

curl -d "@products.json" -H "Content-Type: application/json" -X POST http://localhost:8000/api/create/
