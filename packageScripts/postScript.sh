#!/bin/sh

/usr/bin/su $USER -c  "/usr/sbin/installer -pkg ./RealPackage.pkg -target CurrentUserHomeDirectory"
	
fi

exit 0
