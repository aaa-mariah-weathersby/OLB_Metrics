#!/bin/bash
npm run build
cd build
pm2 delete all
npm install
pm2 startOrRestart ecosystem.json --env production
pm2 log
