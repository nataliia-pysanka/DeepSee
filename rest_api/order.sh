#!/bin/bash

curl -d '{"name":"Brown eggs","amount_in_stock":8}' -H "Content-Type: application/json" -X PUT http://localhost:8000/api/store/
