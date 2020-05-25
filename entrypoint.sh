#!/bin/sh

pulumi login file:///workdir/.pulumi

#pulumi plugin install resource aws v2.5.0

pulumi ${@:-}