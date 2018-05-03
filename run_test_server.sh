#!/bin/bash
npm run build:test
cd build
pm2 delete all
npm install
pm2 startOrRestart ecosystem.json --env test
pm2 log
