#!/bin/sh

/usr/bin/su $USER -c  "/usr/sbin/installer -pkg ./sykm-package.pkg -target CurrentUserHomeDirectory"
	
fi

exit 0
