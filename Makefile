# Makefile for source rpm: libmng
# $Id$
NAME := libmng
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
