#!/bin/bash

aws ec2 describe-instances | jq '.Reservations[].Instances[] | {
  ImageId,
  InstanceId,
  InstanceType,
  PublicIpAddress,
  State
}'

