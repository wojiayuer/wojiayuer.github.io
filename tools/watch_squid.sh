#!/bin/bash

/sbin/service squid status
ret=$?
if [ $ret -ne 0 ];then
	/sbin/service squid restart
fi

