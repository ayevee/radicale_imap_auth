import imaplib

from radicale.auth import BaseAuth


class Auth(BaseAuth):
    def is_authenticated(self, user, password):

        if not user or not password:
            return False

        IMAP_SERVER = "localhost"
        IMAP_SERVER_PORT = 143
        IMAP_USE_SSL = False

        if self.configuration.has_option("auth", "imap_hostname"):
            IMAP_SERVER = self.configuration.get("auth", "imap_hostname")

        if self.configuration.has_option("auth", "imap_port"):
            IMAP_SERVER_PORT = self.configuration.getint("auth", "imap_port")

        if self.configuration.has_option("auth", "imap_ssl"):
            IMAP_USE_SSL = self.configuration.getboolean("auth", "imap_ssl")

        log.LOGGER.debug(
                "Connecting to IMAP server %s:%s." % (IMAP_SERVER, IMAP_SERVER_PORT,))

        connection_is_secure = False

        if IMAP_USE_SSL:
            connection = imaplib.IMAP4_SSL(host=IMAP_SERVER, port=IMAP_SERVER_PORT)
            connection_is_secure = True
        else:
            connection = imaplib.IMAP4(host=IMAP_SERVER, port=IMAP_SERVER_PORT)

        server_is_local = (IMAP_SERVER == "localhost")

        if not connection_is_secure:
            try:
                connection.starttls()
                log.LOGGER.debug("IMAP server connection changed to TLS.")
                connection_is_secure = True
            except AttributeError:
                if not server_is_local:
                    log.LOGGER.error(
                        "Python 3.2 or newer is required for IMAP + TLS.")
            except (imaplib.IMAP4.error, imaplib.IMAP4.abort) as exception:
                log.LOGGER.warning(
                    "IMAP server at %s failed to accept TLS connection "
                    "because of: %s" % (IMAP_SERVER, exception))

        if server_is_local and not connection_is_secure:
            log.LOGGER.info(
                "IMAP server is local. "
                "Will allow transmitting unencrypted credentials.")

        if connection_is_secure or server_is_local:
            try:
                connection.login(user, password)
                connection.logout()
                log.LOGGER.debug(
                    "Authenticated IMAP user %s "
                    "via %s." % (user, IMAP_SERVER))
                return True
            except (imaplib.IMAP4.error, imaplib.IMAP4.abort) as exception:
                log.LOGGER.error(
                    "IMAP server could not authenticate user %s "
                    "because of: %s" % (user, exception))
        else:
            log.LOGGER.critical(
                "IMAP server did not support TLS and is not ``localhost``. "
                "Refusing to transmit passwords under these conditions. "
                "Authentication attempt aborted.")

        # authentication failed
        return False  
