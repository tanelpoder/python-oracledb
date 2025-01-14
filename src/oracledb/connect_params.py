#------------------------------------------------------------------------------
# Copyright (c) 2021, 2022, Oracle and/or its affiliates.
#
# This software is dual-licensed to you under the Universal Permissive License
# (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl and Apache License
# 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose
# either license.
#
# If you elect to accept the software under the Apache License, Version 2.0,
# the following applies:
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# connect_params.py
#
# Contains the ConnectParams class used for managing the parameters required to
# establish a connection to the database.
#
# *** NOTICE *** This file is generated from a template and should not be
# modified directly. See build_from_template.py in the utils subdirectory for
# more information.
#------------------------------------------------------------------------------

import functools
from typing import Type, Union

import oracledb

from . import base_impl, constants, errors, utils

class ConnectParams:
    """
    Contains all parameters used for establishing a connection to the
    database.
    """
    __module__ = oracledb.__name__
    __slots__ = ["_impl"]
    _impl_class = base_impl.ConnectParamsImpl

    @utils.params_initer
    def __init__(self, *,
                 user: str=None,
                 proxy_user: str=None,
                 password: str=None,
                 newpassword: str=None,
                 wallet_password: str=None,
                 host: str=None,
                 port: int=1521,
                 protocol: str="tcp",
                 https_proxy: str=None,
                 https_proxy_port: int=0,
                 service_name: str=None,
                 sid: str=None,
                 server_type: str=None,
                 cclass: str=None,
                 purity: int=oracledb.PURITY_DEFAULT,
                 expire_time: int=0,
                 retry_count: int=0,
                 retry_delay: int=0,
                 tcp_connect_timeout: float=60.0,
                 ssl_server_dn_match: bool=True,
                 ssl_server_cert_dn: str=None,
                 wallet_location: str=None,
                 events: bool=False,
                 externalauth: bool=False,
                 mode: int=oracledb.AUTH_MODE_DEFAULT,
                 disable_oob: bool=False,
                 stmtcachesize: int=oracledb.defaults.stmtcachesize,
                 edition: str=None,
                 tag: str=None,
                 matchanytag: bool=False,
                 config_dir: str=oracledb.defaults.config_dir,
                 appcontext: list=None,
                 shardingkey: list=None,
                 supershardingkey: list=None,
                 debug_jdwp: str=None,
                 handle: int=0,
                 threaded: bool=True,
                 encoding: str=None,
                 nencoding: str=None
                ):
        """
        All parameters are optional. A brief description of each parameter
        follows:

        - user: the name of the user to connect to (default: None)

        - proxy_user: the name of the proxy user to connect to. If this value
          is not specified, it will be parsed out of user if user is in the
          form "user[proxy_user]" (default: None)

        - password: the password for the user (default: None)

        - newpassword: the new password for the user. The new password will
          take effect immediately upon a successful connection to the database
          (default: None)

        - wallet_password: the password to use to decrypt the wallet, if it is
          encrypted. This value is only used in thin mode (default: None)

        - host: the name or IP address of the machine hosting the database or
          the database listener (default: None)

        - port: the port number on which the database listener is listening
          (default: 1521)

        - protocol: one of the strings "tcp" or "tcps" indicating whether to
          use unencrypted network traffic or encrypted network traffic (TLS)
          (default: "tcp")

        - https_proxy: the name or IP address of a proxy host to use for
          tunneling secure connections (default: None)

        - https_proxy_port: the port on which to communicate with the proxy
          host (default: 0)

        - service_name: the service name of the database (default: None)

        - sid: the system identifier (SID) of the database. Note using a
          service_name instead is recommended (default: None)

        - server_type: the type of server connection that should be
          established. If specified, it should be one of "dedicated", "shared"
          or "pooled" (default: None)

        - cclass: connection class to use for Database Resident Connection
          Pooling (DRCP) (default: None)

        - purity: purity to use for Database Resident Connection Pooling (DRCP)
          (default: oracledb.PURITY_DEFAULT)

        - expire_time: an integer indicating the number of minutes between the
          sending of keepalive probes. If this parameter is set to a value
          greater than zero it enables keepalive (default: 0)

        - retry_count: the number of times that a connection attempt should be
          retried before the attempt is terminated (default: 0)

        - retry_delay: the number of seconds to wait before making a new
          connection attempt (default: 0)

        - tcp_connect_timeout: a float indicating the maximum number of seconds
          to wait for establishing a connection to the database host (default:
          60.0)

        - ssl_server_dn_match: boolean indicating whether the server
          certificate distinguished name (DN) should be matched in addition to
          the regular certificate verification that is performed. Note that if
          the ssl_server_cert_dn parameter is not privided, host name matching
          is performed instead (default: True)

        - ssl_server_cert_dn: the distinguished name (DN) which should be
          matched with the server. This value is ignored if the
          ssl_server_dn_match parameter is not set to the value True. If
          specified this value is used for any verfication. Otherwise the
          hostname will be used. (default: None)

        - wallet_location: the directory where the wallet can be found. In thin
          mode this must be the directory containing the PEM-encoded wallet
          file ewallet.pem. In thick mode this must be the directory containing
          the file cwallet.sso (default: None)

        - events: boolean specifying whether events mode should be enabled.
          This value is only used in thick mode and is needed for continuous
          query notification and high availability event notifications
          (default: False)

        - externalauth: a boolean indicating whether to use external
          authentication (default: False)

        - mode: authorization mode to use. For example
          oracledb.AUTH_MODE_SYSDBA (default: oracledb.AUTH_MODE_DEFAULT)

        - disable_oob: boolean indicating whether out-of-band breaks should be
          disabled. This value is only used in thin mode. It has no effect on
          Windows which does not support this functionality (default: False)

        - stmtcachesize: identifies the initial size of the statement cache
          (default: oracledb.defaults.stmtcachesize)

        - edition: edition to use for the connection. This parameter cannot be
          used simultaneously with the cclass parameter (default: None)

        - tag: identifies the type of connection that should be returned from a
          pool. This value is only used in thick mode (default: None)

        - matchanytag: boolean specifying whether any tag can be used when
          acquiring a connection from the pool. This value is only used in
          thick mode. (default: False)

        - config_dir: directory in which the optional tnsnames.ora
          configuration file is located. This value is only used in thin mode.
          For thick mode use the config_dir parameter of init_oracle_client()
          (default: oracledb.defaults.config_dir)

        - appcontext: application context used by the connection. It should be
          a list of 3-tuples (namespace, name, value) and each entry in the
          tuple should be a string. This value is only used in thick mode
          (default: None)

        - shardingkey: a list of strings, numbers, bytes or dates that identify
          the database shard to connect to. This value is only used in thick
          mode (default: None)

        - supershardingkey: a list of strings, numbers, bytes or dates that
          identify the database shard to connect to. This value is only used in
          thick mode (default: None)

        - debug_jdwp: a string with the format "host=<host>;port=<port>" that
          specifies the host and port of the PL/SQL debugger. This value is
          only used in thin mode. For thick mode set the ORA_DEBUG_JDWP
          environment variable (default: None)

        - handle: an integer representing a pointer to a valid service context
          handle. This value is only used in thick mode. It should be used with
          extreme caution (default: 0)
        """
        pass

    def __repr__(self):
        return self.__class__.__qualname__ + "(" + \
               f"user={self.user!r}, " + \
               f"proxy_user={self.proxy_user!r}, " + \
               f"host={self.host!r}, " + \
               f"port={self.port!r}, " + \
               f"protocol={self.protocol!r}, " + \
               f"https_proxy={self.https_proxy!r}, " + \
               f"https_proxy_port={self.https_proxy_port!r}, " + \
               f"service_name={self.service_name!r}, " + \
               f"sid={self.sid!r}, " + \
               f"server_type={self.server_type!r}, " + \
               f"cclass={self.cclass!r}, " + \
               f"purity={self.purity!r}, " + \
               f"expire_time={self.expire_time!r}, " + \
               f"retry_count={self.retry_count!r}, " + \
               f"retry_delay={self.retry_delay!r}, " + \
               f"tcp_connect_timeout={self.tcp_connect_timeout!r}, " + \
               f"ssl_server_dn_match={self.ssl_server_dn_match!r}, " + \
               f"ssl_server_cert_dn={self.ssl_server_cert_dn!r}, " + \
               f"wallet_location={self.wallet_location!r}, " + \
               f"events={self.events!r}, " + \
               f"externalauth={self.externalauth!r}, " + \
               f"mode={self.mode!r}, " + \
               f"disable_oob={self.disable_oob!r}, " + \
               f"stmtcachesize={self.stmtcachesize!r}, " + \
               f"edition={self.edition!r}, " + \
               f"tag={self.tag!r}, " + \
               f"matchanytag={self.matchanytag!r}, " + \
               f"config_dir={self.config_dir!r}, " + \
               f"appcontext={self.appcontext!r}, " + \
               f"shardingkey={self.shardingkey!r}, " + \
               f"supershardingkey={self.supershardingkey!r}, " + \
               f"debug_jdwp={self.debug_jdwp!r}" + \
               ")"

    def _address_attr(f):
        """
        Helper function used to get address level attributes.
        """
        @functools.wraps(f)
        def wrapped(self):
            values = [getattr(a, f.__name__) \
                      for a in self._impl._get_addresses()]
            return values if len(values) > 1 else values[0]
        return wrapped

    def _description_attr(f):
        """
        Helper function used to get description level attributes.
        """
        @functools.wraps(f)
        def wrapped(self):
            values = [getattr(d, f.__name__) \
                      for d in self._impl.description_list.descriptions]
            return values if len(values) > 1 else values[0]
        return wrapped

    @property
    def appcontext(self) -> list:
        """
        Application context used by the connection. It should be a list of
        3-tuples (namespace, name, value) and each entry in the tuple should be
        a string. This value is only used in thick mode.
        """
        return self._impl.appcontext

    @property
    @_description_attr
    def cclass(self) -> Union[list, str]:
        """
        Connection class to use for Database Resident Connection Pooling
        (DRCP).
        """
        return self._impl.cclass

    @property
    def config_dir(self) -> str:
        """
        Directory in which the optional tnsnames.ora configuration file is
        located. This value is only used in thin mode. For thick mode use the
        config_dir parameter of init_oracle_client().
        """
        return self._impl.config_dir

    @property
    def debug_jdwp(self) -> str:
        """
        A string with the format "host=<host>;port=<port>" that specifies the
        host and port of the PL/SQL debugger. This value is only used in thin
        mode. For thick mode set the ORA_DEBUG_JDWP environment variable.
        """
        return self._impl.debug_jdwp

    @property
    def disable_oob(self) -> bool:
        """
        Boolean indicating whether out-of-band breaks should be disabled. This
        value is only used in thin mode. It has no effect on Windows which does
        not support this functionality.
        """
        return self._impl.disable_oob

    @property
    def edition(self) -> str:
        """
        Edition to use for the connection. This parameter cannot be used
        simultaneously with the cclass parameter.
        """
        return self._impl.edition

    @property
    def events(self) -> bool:
        """
        Boolean specifying whether events mode should be enabled. This value is
        only used in thick mode and is needed for continuous query notification
        and high availability event notifications.
        """
        return self._impl.events

    @property
    @_description_attr
    def expire_time(self) -> Union[list, int]:
        """
        An integer indicating the number of minutes between the sending of
        keepalive probes. If this parameter is set to a value greater than zero
        it enables keepalive.
        """
        return self._impl.expire_time

    @property
    def externalauth(self) -> bool:
        """
        A boolean indicating whether to use external authentication.
        """
        return self._impl.externalauth

    @property
    @_address_attr
    def host(self) -> Union[list, str]:
        """
        The name or IP address of the machine hosting the database or the
        database listener.
        """
        return self._impl.host

    @property
    @_address_attr
    def https_proxy(self) -> Union[list, str]:
        """
        The name or IP address of a proxy host to use for tunneling secure
        connections.
        """
        return self._impl.https_proxy

    @property
    @_address_attr
    def https_proxy_port(self) -> Union[list, int]:
        """
        The port on which to communicate with the proxy host.
        """
        return self._impl.https_proxy_port

    @property
    def matchanytag(self) -> bool:
        """
        Boolean specifying whether any tag can be used when acquiring a
        connection from the pool. This value is only used in thick mode..
        """
        return self._impl.matchanytag

    @property
    def mode(self) -> int:
        """
        Authorization mode to use. For example oracledb.AUTH_MODE_SYSDBA.
        """
        return self._impl.mode

    @property
    @_address_attr
    def port(self) -> Union[list, int]:
        """
        The port number on which the database listener is listening.
        """
        return self._impl.port

    @property
    @_address_attr
    def protocol(self) -> Union[list, str]:
        """
        One of the strings "tcp" or "tcps" indicating whether to use
        unencrypted network traffic or encrypted network traffic (TLS).
        """
        return self._impl.protocol

    @property
    def proxy_user(self) -> str:
        """
        The name of the proxy user to connect to. If this value is not
        specified, it will be parsed out of user if user is in the form
        "user[proxy_user]".
        """
        return self._impl.proxy_user

    @property
    @_description_attr
    def purity(self) -> Union[list, int]:
        """
        Purity to use for Database Resident Connection Pooling (DRCP).
        """
        return self._impl.purity

    @property
    @_description_attr
    def retry_count(self) -> Union[list, int]:
        """
        The number of times that a connection attempt should be retried before
        the attempt is terminated.
        """
        return self._impl.retry_count

    @property
    @_description_attr
    def retry_delay(self) -> Union[list, int]:
        """
        The number of seconds to wait before making a new connection attempt.
        """
        return self._impl.retry_delay

    @property
    @_description_attr
    def server_type(self) -> Union[list, str]:
        """
        The type of server connection that should be established. If specified,
        it should be one of "dedicated", "shared" or "pooled".
        """
        return self._impl.server_type

    @property
    @_description_attr
    def service_name(self) -> Union[list, str]:
        """
        The service name of the database.
        """
        return self._impl.service_name

    @property
    def shardingkey(self) -> list:
        """
        A list of strings, numbers, bytes or dates that identify the database
        shard to connect to. This value is only used in thick mode.
        """
        return self._impl.shardingkey

    @property
    @_description_attr
    def sid(self) -> Union[list, str]:
        """
        The system identifier (SID) of the database. Note using a service_name
        instead is recommended.
        """
        return self._impl.sid

    @property
    @_description_attr
    def ssl_server_cert_dn(self) -> Union[list, str]:
        """
        The distinguished name (DN) which should be matched with the server.
        This value is ignored if the ssl_server_dn_match parameter is not set
        to the value True. If specified this value is used for any verfication.
        Otherwise the hostname will be used..
        """
        return self._impl.ssl_server_cert_dn

    @property
    @_description_attr
    def ssl_server_dn_match(self) -> Union[list, bool]:
        """
        Boolean indicating whether the server certificate distinguished name
        (DN) should be matched in addition to the regular certificate
        verification that is performed. Note that if the ssl_server_cert_dn
        parameter is not privided, host name matching is performed instead.
        """
        return self._impl.ssl_server_dn_match

    @property
    def stmtcachesize(self) -> int:
        """
        Identifies the initial size of the statement cache.
        """
        return self._impl.stmtcachesize

    @property
    def supershardingkey(self) -> list:
        """
        A list of strings, numbers, bytes or dates that identify the database
        shard to connect to. This value is only used in thick mode.
        """
        return self._impl.supershardingkey

    @property
    def tag(self) -> str:
        """
        Identifies the type of connection that should be returned from a pool.
        This value is only used in thick mode.
        """
        return self._impl.tag

    @property
    @_description_attr
    def tcp_connect_timeout(self) -> Union[list, float]:
        """
        A float indicating the maximum number of seconds to wait for
        establishing a connection to the database host.
        """
        return self._impl.tcp_connect_timeout

    @property
    def user(self) -> str:
        """
        The name of the user to connect to.
        """
        return self._impl.user

    @property
    @_description_attr
    def wallet_location(self) -> Union[list, str]:
        """
        The directory where the wallet can be found. In thin mode this must be
        the directory containing the PEM-encoded wallet file ewallet.pem. In
        thick mode this must be the directory containing the file cwallet.sso.
        """
        return self._impl.wallet_location

    def copy(self) -> Type["ConnectParams"]:
        """
        Creates a copy of the parameters and returns it.
        """
        params = ConnectParams.__new__(ConnectParams)
        params._impl = self._impl.copy()
        return params

    def get_connect_string(self) -> str:
        """
        Returns a connect string generated from the parameters.
        """
        return self._impl.get_connect_string()

    def parse_connect_string(self, connect_string: str) -> None:
        """
        Parses the connect string into its components and stores the
        parameters.  The connect string could be an Easy Connect string,
        name-value pairs or a simple alias which is looked up in tnsnames.ora.
        Any parameters found in the connect string override any currently
        stored values.
        """
        self._impl.parse_connect_string(connect_string)

    @utils.params_setter
    def set(self, *,
            user: str=None,
            proxy_user: str=None,
            password: str=None,
            newpassword: str=None,
            wallet_password: str=None,
            host: str=None,
            port: int=None,
            protocol: str=None,
            https_proxy: str=None,
            https_proxy_port: int=None,
            service_name: str=None,
            sid: str=None,
            server_type: str=None,
            cclass: str=None,
            purity: int=None,
            expire_time: int=None,
            retry_count: int=None,
            retry_delay: int=None,
            tcp_connect_timeout: float=None,
            ssl_server_dn_match: bool=None,
            ssl_server_cert_dn: str=None,
            wallet_location: str=None,
            events: bool=None,
            externalauth: bool=None,
            mode: int=None,
            disable_oob: bool=None,
            stmtcachesize: int=None,
            edition: str=None,
            tag: str=None,
            matchanytag: bool=None,
            config_dir: str=None,
            appcontext: list=None,
            shardingkey: list=None,
            supershardingkey: list=None,
            debug_jdwp: str=None,
            handle: int=None,
            threaded: bool=None,
            encoding: str=None,
            nencoding: str=None
           ):
        """
        All parameters are optional. A brief description of each parameter
        follows:

        - user: the name of the user to connect to

        - proxy_user: the name of the proxy user to connect to. If this value
          is not specified, it will be parsed out of user if user is in the
          form "user[proxy_user]"

        - password: the password for the user

        - newpassword: the new password for the user. The new password will
          take effect immediately upon a successful connection to the database

        - wallet_password: the password to use to decrypt the wallet, if it is
          encrypted. This value is only used in thin mode

        - host: the name or IP address of the machine hosting the database or
          the database listener

        - port: the port number on which the database listener is listening

        - protocol: one of the strings "tcp" or "tcps" indicating whether to
          use unencrypted network traffic or encrypted network traffic (TLS)

        - https_proxy: the name or IP address of a proxy host to use for
          tunneling secure connections

        - https_proxy_port: the port on which to communicate with the proxy
          host

        - service_name: the service name of the database

        - sid: the system identifier (SID) of the database. Note using a
          service_name instead is recommended

        - server_type: the type of server connection that should be
          established. If specified, it should be one of "dedicated", "shared"
          or "pooled"

        - cclass: connection class to use for Database Resident Connection
          Pooling (DRCP)

        - purity: purity to use for Database Resident Connection Pooling (DRCP)

        - expire_time: an integer indicating the number of minutes between the
          sending of keepalive probes. If this parameter is set to a value
          greater than zero it enables keepalive

        - retry_count: the number of times that a connection attempt should be
          retried before the attempt is terminated

        - retry_delay: the number of seconds to wait before making a new
          connection attempt

        - tcp_connect_timeout: a float indicating the maximum number of seconds
          to wait for establishing a connection to the database host

        - ssl_server_dn_match: boolean indicating whether the server
          certificate distinguished name (DN) should be matched in addition to
          the regular certificate verification that is performed. Note that if
          the ssl_server_cert_dn parameter is not privided, host name matching
          is performed instead

        - ssl_server_cert_dn: the distinguished name (DN) which should be
          matched with the server. This value is ignored if the
          ssl_server_dn_match parameter is not set to the value True. If
          specified this value is used for any verfication. Otherwise the
          hostname will be used.

        - wallet_location: the directory where the wallet can be found. In thin
          mode this must be the directory containing the PEM-encoded wallet
          file ewallet.pem. In thick mode this must be the directory containing
          the file cwallet.sso

        - events: boolean specifying whether events mode should be enabled.
          This value is only used in thick mode and is needed for continuous
          query notification and high availability event notifications

        - externalauth: a boolean indicating whether to use external
          authentication

        - mode: authorization mode to use. For example
          oracledb.AUTH_MODE_SYSDBA

        - disable_oob: boolean indicating whether out-of-band breaks should be
          disabled. This value is only used in thin mode. It has no effect on
          Windows which does not support this functionality

        - stmtcachesize: identifies the initial size of the statement cache

        - edition: edition to use for the connection. This parameter cannot be
          used simultaneously with the cclass parameter

        - tag: identifies the type of connection that should be returned from a
          pool. This value is only used in thick mode

        - matchanytag: boolean specifying whether any tag can be used when
          acquiring a connection from the pool. This value is only used in
          thick mode.

        - config_dir: directory in which the optional tnsnames.ora
          configuration file is located. This value is only used in thin mode.
          For thick mode use the config_dir parameter of init_oracle_client()

        - appcontext: application context used by the connection. It should be
          a list of 3-tuples (namespace, name, value) and each entry in the
          tuple should be a string. This value is only used in thick mode

        - shardingkey: a list of strings, numbers, bytes or dates that identify
          the database shard to connect to. This value is only used in thick
          mode

        - supershardingkey: a list of strings, numbers, bytes or dates that
          identify the database shard to connect to. This value is only used in
          thick mode

        - debug_jdwp: a string with the format "host=<host>;port=<port>" that
          specifies the host and port of the PL/SQL debugger. This value is
          only used in thin mode. For thick mode set the ORA_DEBUG_JDWP
          environment variable

        - handle: an integer representing a pointer to a valid service context
          handle. This value is only used in thick mode. It should be used with
          extreme caution
        """
        pass
