#
# This file is part of pysnmp software.
#
# Copyright (c) 2005-2016, Ilya Etingof <ilya@glas.net>
# License: http://pysnmp.sf.net/license.html
#
# PySNMP MIB module SNMP-USER-BASED-SM-MIB (http://pysnmp.sf.net)
# ASN.1 source file:///usr/share/snmp/mibs/SNMP-USER-BASED-SM-MIB.txt
# Produced by pysmi-0.0.5 at Sat Sep 19 23:10:57 2015
# On host grommit.local platform Darwin version 14.4.0 by user ilya
# Using Python version 2.7.6 (default, Sep  9 2014, 15:04:36) 
#
(Integer, ObjectIdentifier, OctetString,) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier",
                                                                     "OctetString")
(NamedValues,) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
(ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint,
 ValueRangeConstraint,) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint",
                                                   "ConstraintsIntersection", "ValueSizeConstraint",
                                                   "ValueRangeConstraint")
(SnmpAdminString, snmpPrivProtocols, snmpAuthProtocols, SnmpEngineID,) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB",
                                                                                                  "SnmpAdminString",
                                                                                                  "snmpPrivProtocols",
                                                                                                  "snmpAuthProtocols",
                                                                                                  "SnmpEngineID")
(NotificationGroup, ModuleCompliance, ObjectGroup,) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup",
                                                                               "ModuleCompliance", "ObjectGroup")
(Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks,
 Counter64, Unsigned32, ModuleIdentity, Gauge32, snmpModules, iso, ObjectIdentity, Bits,
 Counter32,) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow",
                                        "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks",
                                        "Counter64", "Unsigned32", "ModuleIdentity", "Gauge32", "snmpModules", "iso",
                                        "ObjectIdentity", "Bits", "Counter32")
(TextualConvention, AutonomousType, StorageType, TestAndIncr, RowStatus, DisplayString,
 RowPointer,) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "AutonomousType", "StorageType",
                                         "TestAndIncr", "RowStatus", "DisplayString", "RowPointer")
snmpUsmMIB = ModuleIdentity((1, 3, 6, 1, 6, 3, 15)).setRevisions(
    ("2002-10-16 00:00", "1999-01-20 00:00", "1997-11-20 00:00",))
if mibBuilder.loadTexts:
    snmpUsmMIB.setLastUpdated('200210160000Z')
if mibBuilder.loadTexts:
    snmpUsmMIB.setOrganization('SNMPv3 Working Group')
if mibBuilder.loadTexts:
    snmpUsmMIB.setContactInfo(
        'WG-email:   snmpv3@lists.tislabs.com\n                  Subscribe:  majordomo@lists.tislabs.com\n                              In msg body:  subscribe snmpv3\n\n                  Chair:      Russ Mundy\n                              Network Associates Laboratories\n                  postal:     15204 Omega Drive, Suite 300\n                              Rockville, MD 20850-4601\n                              USA\n                  email:      mundy@tislabs.com\n\n                  phone:      +1 301-947-7107\n\n                  Co-Chair:   David Harrington\n                              Enterasys Networks\n                  Postal:     35 Industrial Way\n                              P. O. Box 5004\n                              Rochester, New Hampshire 03866-5005\n                              USA\n                  EMail:      dbh@enterasys.com\n                  Phone:      +1 603-337-2614\n\n                  Co-editor   Uri Blumenthal\n                              Lucent Technologies\n                  postal:     67 Whippany Rd.\n                              Whippany, NJ 07981\n                              USA\n                  email:      uri@lucent.com\n                  phone:      +1-973-386-2163\n\n                  Co-editor:  Bert Wijnen\n                              Lucent Technologies\n                  postal:     Schagen 33\n                              3461 GL Linschoten\n                              Netherlands\n                  email:      bwijnen@lucent.com\n                  phone:      +31-348-480-685\n                 ')
if mibBuilder.loadTexts:
    snmpUsmMIB.setDescription(
        'The management information definitions for the\n                  SNMP User-based Security Model.\n\n                  Copyright (C) The Internet Society (2002). This\n                  version of this MIB module is part of RFC 3414;\n                  see the RFC itself for full legal notices.\n                 ')
usmMIBObjects = MibIdentifier((1, 3, 6, 1, 6, 3, 15, 1))
usmMIBConformance = MibIdentifier((1, 3, 6, 1, 6, 3, 15, 2))
usmNoAuthProtocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 1, 1))
if mibBuilder.loadTexts:
    usmNoAuthProtocol.setDescription('No Authentication Protocol.')
usmHMACMD5AuthProtocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 1, 2))
if mibBuilder.loadTexts:
    usmHMACMD5AuthProtocol.setDescription('The HMAC-MD5-96 Digest Authentication Protocol.')
usmHMACSHAAuthProtocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 1, 3))
if mibBuilder.loadTexts:
    usmHMACSHAAuthProtocol.setDescription('The HMAC-SHA-96 Digest Authentication Protocol.')
usmNoPrivProtocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 2, 1))
if mibBuilder.loadTexts:
    usmNoPrivProtocol.setDescription('No Privacy Protocol.')
usmDESPrivProtocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 2, 2))
if mibBuilder.loadTexts:
    usmDESPrivProtocol.setDescription('The CBC-DES Symmetric Encryption Protocol.')


class KeyChange(OctetString, TextualConvention):
    pass


usmStats = MibIdentifier((1, 3, 6, 1, 6, 3, 15, 1, 1))
usmStatsUnsupportedSecLevels = MibScalar((1, 3, 6, 1, 6, 3, 15, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    usmStatsUnsupportedSecLevels.setDescription(
        'The total number of packets received by the SNMP\n                 engine which were dropped because they requested a\n                 securityLevel that was unknown to the SNMP engine\n                 or otherwise unavailable.\n                ')
usmStatsNotInTimeWindows = MibScalar((1, 3, 6, 1, 6, 3, 15, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    usmStatsNotInTimeWindows.setDescription(
        "The total number of packets received by the SNMP\n                 engine which were dropped because they appeared\n                 outside of the authoritative SNMP engine's window.\n                ")
usmStatsUnknownUserNames = MibScalar((1, 3, 6, 1, 6, 3, 15, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    usmStatsUnknownUserNames.setDescription(
        'The total number of packets received by the SNMP\n                 engine which were dropped because they referenced a\n                 user that was not known to the SNMP engine.\n                ')
usmStatsUnknownEngineIDs = MibScalar((1, 3, 6, 1, 6, 3, 15, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    usmStatsUnknownEngineIDs.setDescription(
        'The total number of packets received by the SNMP\n                 engine which were dropped because they referenced an\n                 snmpEngineID that was not known to the SNMP engine.\n                ')
usmStatsWrongDigests = MibScalar((1, 3, 6, 1, 6, 3, 15, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    usmStatsWrongDigests.setDescription(
        "The total number of packets received by the SNMP\n                 engine which were dropped because they didn't\n                 contain the expected digest value.\n                ")
usmStatsDecryptionErrors = MibScalar((1, 3, 6, 1, 6, 3, 15, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    usmStatsDecryptionErrors.setDescription(
        'The total number of packets received by the SNMP\n                 engine which were dropped because they could not be\n                 decrypted.\n                ')
usmUser = MibIdentifier((1, 3, 6, 1, 6, 3, 15, 1, 2))
usmUserSpinLock = MibScalar((1, 3, 6, 1, 6, 3, 15, 1, 2, 1), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    usmUserSpinLock.setDescription(
        'An advisory lock used to allow several cooperating\n                 Command Generator Applications to coordinate their\n                 use of facilities to alter secrets in the\n                 usmUserTable.\n                ')
usmUserTable = MibTable((1, 3, 6, 1, 6, 3, 15, 1, 2, 2), )
if mibBuilder.loadTexts:
    usmUserTable.setDescription(
        "The table of users configured in the SNMP engine's\n                 Local Configuration Datastore (LCD).\n\n                 To create a new user (i.e., to instantiate a new\n                 conceptual row in this table), it is recommended to\n                 follow this procedure:\n\n                   1)  GET(usmUserSpinLock.0) and save in sValue.\n\n                   2)  SET(usmUserSpinLock.0=sValue,\n                           usmUserCloneFrom=templateUser,\n                           usmUserStatus=createAndWait)\n                       You should use a template user to clone from\n                       which has the proper auth/priv protocol defined.\n\n                 If the new user is to use privacy:\n\n                   3)  generate the keyChange value based on the secret\n                       privKey of the clone-from user and the secret key\n                       to be used for the new user. Let us call this\n                       pkcValue.\n                   4)  GET(usmUserSpinLock.0) and save in sValue.\n                   5)  SET(usmUserSpinLock.0=sValue,\n                           usmUserPrivKeyChange=pkcValue\n                           usmUserPublic=randomValue1)\n                   6)  GET(usmUserPulic) and check it has randomValue1.\n                       If not, repeat steps 4-6.\n\n                 If the new user will never use privacy:\n\n                   7)  SET(usmUserPrivProtocol=usmNoPrivProtocol)\n\n                 If the new user is to use authentication:\n\n                   8)  generate the keyChange value based on the secret\n                       authKey of the clone-from user and the secret key\n                       to be used for the new user. Let us call this\n                       akcValue.\n                   9)  GET(usmUserSpinLock.0) and save in sValue.\n                   10) SET(usmUserSpinLock.0=sValue,\n                           usmUserAuthKeyChange=akcValue\n                           usmUserPublic=randomValue2)\n                   11) GET(usmUserPulic) and check it has randomValue2.\n                       If not, repeat steps 9-11.\n\n                 If the new user will never use authentication:\n\n                   12) SET(usmUserAuthProtocol=usmNoAuthProtocol)\n\n                 Finally, activate the new user:\n\n                   13) SET(usmUserStatus=active)\n\n                 The new user should now be available and ready to be\n                 used for SNMPv3 communication. Note however that access\n                 to MIB data must be provided via configuration of the\n                 SNMP-VIEW-BASED-ACM-MIB.\n\n                 The use of usmUserSpinlock is to avoid conflicts with\n                 another SNMP command generator application which may\n                 also be acting on the usmUserTable.\n                ")
usmUserEntry = MibTableRow((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1), ).setIndexNames(
    (0, "SNMP-USER-BASED-SM-MIB", "usmUserEngineID"), (0, "SNMP-USER-BASED-SM-MIB", "usmUserName"))
if mibBuilder.loadTexts:
    usmUserEntry.setDescription(
        "A user configured in the SNMP engine's Local\n                 Configuration Datastore (LCD) for the User-based\n                 Security Model.\n                ")
usmUserEngineID = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 1), SnmpEngineID())
if mibBuilder.loadTexts:
    usmUserEngineID.setDescription(
        "An SNMP engine's administratively-unique identifier.\n\n                 In a simple agent, this value is always that agent's\n                 own snmpEngineID value.\n\n                 The value can also take the value of the snmpEngineID\n                 of a remote SNMP engine with which this user can\n                 communicate.\n                ")
usmUserName = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 2),
                             SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts:
    usmUserName.setDescription(
        'A human readable string representing the name of\n                 the user.\n\n                 This is the (User-based Security) Model dependent\n                 security ID.\n                ')
usmUserSecurityName = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    usmUserSecurityName.setDescription(
        'A human readable string representing the user in\n                 Security Model independent format.\n\n                 The default transformation of the User-based Security\n                 Model dependent security ID to the securityName and\n                 vice versa is the identity function so that the\n                 securityName is the same as the userName.\n                ')
usmUserCloneFrom = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 4), RowPointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    usmUserCloneFrom.setDescription(
        "A pointer to another conceptual row in this\n                 usmUserTable.  The user in this other conceptual\n                 row is called the clone-from user.\n\n                 When a new user is created (i.e., a new conceptual\n                 row is instantiated in this table), the privacy and\n                 authentication parameters of the new user must be\n                 cloned from its clone-from user. These parameters are:\n                   - authentication protocol (usmUserAuthProtocol)\n                   - privacy protocol (usmUserPrivProtocol)\n                 They will be copied regardless of what the current\n                 value is.\n\n                 Cloning also causes the initial values of the secret\n                 authentication key (authKey) and the secret encryption\n\n                 key (privKey) of the new user to be set to the same\n                 values as the corresponding secrets of the clone-from\n                 user to allow the KeyChange process to occur as\n                 required during user creation.\n\n                 The first time an instance of this object is set by\n                 a management operation (either at or after its\n                 instantiation), the cloning process is invoked.\n                 Subsequent writes are successful but invoke no\n                 action to be taken by the receiver.\n                 The cloning process fails with an 'inconsistentName'\n                 error if the conceptual row representing the\n                 clone-from user does not exist or is not in an active\n                 state when the cloning process is invoked.\n\n                 When this object is read, the ZeroDotZero OID\n                 is returned.\n                ")
usmUserAuthProtocol = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 5),
                                     AutonomousType().clone((1, 3, 6, 1, 6, 3, 10, 1, 1, 1))).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    usmUserAuthProtocol.setDescription(
        "An indication of whether messages sent on behalf of\n                 this user to/from the SNMP engine identified by\n                 usmUserEngineID, can be authenticated, and if so,\n                 the type of authentication protocol which is used.\n\n                 An instance of this object is created concurrently\n                 with the creation of any other object instance for\n                 the same user (i.e., as part of the processing of\n                 the set operation which creates the first object\n                 instance in the same conceptual row).\n\n                 If an initial set operation (i.e. at row creation time)\n                 tries to set a value for an unknown or unsupported\n                 protocol, then a 'wrongValue' error must be returned.\n\n                 The value will be overwritten/set when a set operation\n                 is performed on the corresponding instance of\n                 usmUserCloneFrom.\n\n                 Once instantiated, the value of such an instance of\n                 this object can only be changed via a set operation to\n                 the value of the usmNoAuthProtocol.\n\n                 If a set operation tries to change the value of an\n\n                 existing instance of this object to any value other\n                 than usmNoAuthProtocol, then an 'inconsistentValue'\n                 error must be returned.\n\n                 If a set operation tries to set the value to the\n                 usmNoAuthProtocol while the usmUserPrivProtocol value\n                 in the same row is not equal to usmNoPrivProtocol,\n                 then an 'inconsistentValue' error must be returned.\n                 That means that an SNMP command generator application\n                 must first ensure that the usmUserPrivProtocol is set\n                 to the usmNoPrivProtocol value before it can set\n                 the usmUserAuthProtocol value to usmNoAuthProtocol.\n                ")
usmUserAuthKeyChange = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 6),
                                      KeyChange().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    usmUserAuthKeyChange.setDescription(
        "An object, which when modified, causes the secret\n                 authentication key used for messages sent on behalf\n                 of this user to/from the SNMP engine identified by\n                 usmUserEngineID, to be modified via a one-way\n                 function.\n\n                 The associated protocol is the usmUserAuthProtocol.\n                 The associated secret key is the user's secret\n                 authentication key (authKey). The associated hash\n                 algorithm is the algorithm used by the user's\n                 usmUserAuthProtocol.\n\n                 When creating a new user, it is an 'inconsistentName'\n                 error for a set operation to refer to this object\n                 unless it is previously or concurrently initialized\n                 through a set operation on the corresponding instance\n                 of usmUserCloneFrom.\n\n                 When the value of the corresponding usmUserAuthProtocol\n                 is usmNoAuthProtocol, then a set is successful, but\n                 effectively is a no-op.\n\n                 When this object is read, the zero-length (empty)\n                 string is returned.\n\n                 The recommended way to do a key change is as follows:\n\n                   1) GET(usmUserSpinLock.0) and save in sValue.\n                   2) generate the keyChange value based on the old\n                      (existing) secret key and the new secret key,\n                      let us call this kcValue.\n\n                 If you do the key change on behalf of another user:\n\n                   3) SET(usmUserSpinLock.0=sValue,\n                          usmUserAuthKeyChange=kcValue\n                          usmUserPublic=randomValue)\n\n                 If you do the key change for yourself:\n\n                   4) SET(usmUserSpinLock.0=sValue,\n                          usmUserOwnAuthKeyChange=kcValue\n                          usmUserPublic=randomValue)\n\n                 If you get a response with error-status of noError,\n                 then the SET succeeded and the new key is active.\n                 If you do not get a response, then you can issue a\n                 GET(usmUserPublic) and check if the value is equal\n                 to the randomValue you did send in the SET. If so, then\n                 the key change succeeded and the new key is active\n                 (probably the response got lost). If not, then the SET\n                 request probably never reached the target and so you\n                 can start over with the procedure above.\n                ")
usmUserOwnAuthKeyChange = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 7),
                                         KeyChange().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    usmUserOwnAuthKeyChange.setDescription(
        "Behaves exactly as usmUserAuthKeyChange, with one\n                 notable difference: in order for the set operation\n                 to succeed, the usmUserName of the operation\n                 requester must match the usmUserName that\n                 indexes the row which is targeted by this\n                 operation.\n                 In addition, the USM security model must be\n                 used for this operation.\n\n                 The idea here is that access to this column can be\n                 public, since it will only allow a user to change\n                 his own secret authentication key (authKey).\n                 Note that this can only be done once the row is active.\n\n                 When a set is received and the usmUserName of the\n                 requester is not the same as the umsUserName that\n                 indexes the row which is targeted by this operation,\n                 then a 'noAccess' error must be returned.\n\n                 When a set is received and the security model in use\n                 is not USM, then a 'noAccess' error must be returned.\n                ")
usmUserPrivProtocol = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 8),
                                     AutonomousType().clone((1, 3, 6, 1, 6, 3, 10, 1, 2, 1))).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    usmUserPrivProtocol.setDescription(
        "An indication of whether messages sent on behalf of\n                 this user to/from the SNMP engine identified by\n                 usmUserEngineID, can be protected from disclosure,\n                 and if so, the type of privacy protocol which is used.\n\n                 An instance of this object is created concurrently\n                 with the creation of any other object instance for\n                 the same user (i.e., as part of the processing of\n                 the set operation which creates the first object\n                 instance in the same conceptual row).\n\n                 If an initial set operation (i.e. at row creation time)\n                 tries to set a value for an unknown or unsupported\n                 protocol, then a 'wrongValue' error must be returned.\n\n                 The value will be overwritten/set when a set operation\n                 is performed on the corresponding instance of\n                 usmUserCloneFrom.\n\n                 Once instantiated, the value of such an instance of\n                 this object can only be changed via a set operation to\n                 the value of the usmNoPrivProtocol.\n\n                 If a set operation tries to change the value of an\n                 existing instance of this object to any value other\n                 than usmNoPrivProtocol, then an 'inconsistentValue'\n                 error must be returned.\n\n                 Note that if any privacy protocol is used, then you\n                 must also use an authentication protocol. In other\n                 words, if usmUserPrivProtocol is set to anything else\n                 than usmNoPrivProtocol, then the corresponding instance\n                 of usmUserAuthProtocol cannot have a value of\n\n                 usmNoAuthProtocol. If it does, then an\n                 'inconsistentValue' error must be returned.\n                ")
usmUserPrivKeyChange = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 9),
                                      KeyChange().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    usmUserPrivKeyChange.setDescription(
        "An object, which when modified, causes the secret\n                 encryption key used for messages sent on behalf\n                 of this user to/from the SNMP engine identified by\n                 usmUserEngineID, to be modified via a one-way\n                 function.\n\n                 The associated protocol is the usmUserPrivProtocol.\n                 The associated secret key is the user's secret\n                 privacy key (privKey). The associated hash\n                 algorithm is the algorithm used by the user's\n                 usmUserAuthProtocol.\n\n                 When creating a new user, it is an 'inconsistentName'\n                 error for a set operation to refer to this object\n                 unless it is previously or concurrently initialized\n                 through a set operation on the corresponding instance\n                 of usmUserCloneFrom.\n\n                 When the value of the corresponding usmUserPrivProtocol\n                 is usmNoPrivProtocol, then a set is successful, but\n                 effectively is a no-op.\n\n                 When this object is read, the zero-length (empty)\n                 string is returned.\n                 See the description clause of usmUserAuthKeyChange for\n                 a recommended procedure to do a key change.\n                ")
usmUserOwnPrivKeyChange = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 10),
                                         KeyChange().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    usmUserOwnPrivKeyChange.setDescription(
        "Behaves exactly as usmUserPrivKeyChange, with one\n                 notable difference: in order for the Set operation\n                 to succeed, the usmUserName of the operation\n                 requester must match the usmUserName that indexes\n\n                 the row which is targeted by this operation.\n                 In addition, the USM security model must be\n                 used for this operation.\n\n                 The idea here is that access to this column can be\n                 public, since it will only allow a user to change\n                 his own secret privacy key (privKey).\n                 Note that this can only be done once the row is active.\n\n                 When a set is received and the usmUserName of the\n                 requester is not the same as the umsUserName that\n                 indexes the row which is targeted by this operation,\n                 then a 'noAccess' error must be returned.\n\n                 When a set is received and the security model in use\n                 is not USM, then a 'noAccess' error must be returned.\n                ")
usmUserPublic = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 11),
                               OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(
                                   hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    usmUserPublic.setDescription(
        "A publicly-readable value which can be written as part\n                 of the procedure for changing a user's secret\n                 authentication and/or privacy key, and later read to\n                 determine whether the change of the secret was\n                 effected.\n                ")
usmUserStorageType = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 12),
                                    StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    usmUserStorageType.setDescription(
        "The storage type for this conceptual row.\n\n                 Conceptual rows having the value 'permanent' must\n                 allow write-access at a minimum to:\n\n                 - usmUserAuthKeyChange, usmUserOwnAuthKeyChange\n                   and usmUserPublic for a user who employs\n                   authentication, and\n                 - usmUserPrivKeyChange, usmUserOwnPrivKeyChange\n                   and usmUserPublic for a user who employs\n                   privacy.\n\n                 Note that any user who employs authentication or\n                 privacy must allow its secret(s) to be updated and\n                 thus cannot be 'readOnly'.\n\n                 If an initial set operation tries to set the value to\n                 'readOnly' for a user who employs authentication or\n                 privacy, then an 'inconsistentValue' error must be\n                 returned.  Note that if the value has been previously\n                 set (implicit or explicit) to any value, then the rules\n                 as defined in the StorageType Textual Convention apply.\n\n                 It is an implementation issue to decide if a SET for\n                 a readOnly or permanent row is accepted at all. In some\n                 contexts this may make sense, in others it may not. If\n                 a SET for a readOnly or permanent row is not accepted\n                 at all, then a 'wrongValue' error must be returned.\n                ")
usmUserStatus = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    usmUserStatus.setDescription(
        "The status of this conceptual row.\n\n                 Until instances of all corresponding columns are\n                 appropriately configured, the value of the\n                 corresponding instance of the usmUserStatus column\n                 is 'notReady'.\n\n                 In particular, a newly created row for a user who\n                 employs authentication, cannot be made active until the\n                 corresponding usmUserCloneFrom and usmUserAuthKeyChange\n                 have been set.\n\n                 Further, a newly created row for a user who also\n                 employs privacy, cannot be made active until the\n                 usmUserPrivKeyChange has been set.\n\n                 The RowStatus TC [RFC2579] requires that this\n                 DESCRIPTION clause states under which circumstances\n                 other objects in this row can be modified:\n\n                 The value of this object has no effect on whether\n                 other objects in this conceptual row can be modified,\n                 except for usmUserOwnAuthKeyChange and\n                 usmUserOwnPrivKeyChange. For these 2 objects, the\n\n                 value of usmUserStatus MUST be active.\n                ")
usmMIBCompliances = MibIdentifier((1, 3, 6, 1, 6, 3, 15, 2, 1))
usmMIBGroups = MibIdentifier((1, 3, 6, 1, 6, 3, 15, 2, 2))
usmMIBCompliance = ModuleCompliance((1, 3, 6, 1, 6, 3, 15, 2, 1, 1)).setObjects(
    *(("SNMP-USER-BASED-SM-MIB", "usmMIBBasicGroup"),))
if mibBuilder.loadTexts:
    usmMIBCompliance.setDescription(
        'The compliance statement for SNMP engines which\n                 implement the SNMP-USER-BASED-SM-MIB.\n                ')
usmMIBBasicGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 15, 2, 2, 1)).setObjects(
    *(("SNMP-USER-BASED-SM-MIB", "usmStatsUnsupportedSecLevels"), ("SNMP-USER-BASED-SM-MIB", "usmStatsNotInTimeWindows"),
      ("SNMP-USER-BASED-SM-MIB", "usmStatsUnknownUserNames"), ("SNMP-USER-BASED-SM-MIB", "usmStatsUnknownEngineIDs"),
      ("SNMP-USER-BASED-SM-MIB", "usmStatsWrongDigests"), ("SNMP-USER-BASED-SM-MIB", "usmStatsDecryptionErrors"),
      ("SNMP-USER-BASED-SM-MIB", "usmUserSpinLock"), ("SNMP-USER-BASED-SM-MIB", "usmUserSecurityName"),
      ("SNMP-USER-BASED-SM-MIB", "usmUserCloneFrom"), ("SNMP-USER-BASED-SM-MIB", "usmUserAuthProtocol"),
      ("SNMP-USER-BASED-SM-MIB", "usmUserAuthKeyChange"), ("SNMP-USER-BASED-SM-MIB", "usmUserOwnAuthKeyChange"),
      ("SNMP-USER-BASED-SM-MIB", "usmUserPrivProtocol"), ("SNMP-USER-BASED-SM-MIB", "usmUserPrivKeyChange"),
      ("SNMP-USER-BASED-SM-MIB", "usmUserOwnPrivKeyChange"), ("SNMP-USER-BASED-SM-MIB", "usmUserPublic"),
      ("SNMP-USER-BASED-SM-MIB", "usmUserStorageType"), ("SNMP-USER-BASED-SM-MIB", "usmUserStatus"))
)
if mibBuilder.loadTexts:
    usmMIBBasicGroup.setDescription(
        'A collection of objects providing for configuration\n                 of an SNMP engine which implements the SNMP\n                 User-based Security Model.\n                ')
mibBuilder.exportSymbols("SNMP-USER-BASED-SM-MIB", usmUserOwnPrivKeyChange=usmUserOwnPrivKeyChange, usmUser=usmUser,
                         usmStatsUnsupportedSecLevels=usmStatsUnsupportedSecLevels,
                         usmHMACSHAAuthProtocol=usmHMACSHAAuthProtocol, snmpUsmMIB=snmpUsmMIB,
                         usmMIBConformance=usmMIBConformance, usmUserCloneFrom=usmUserCloneFrom,
                         usmUserSecurityName=usmUserSecurityName, usmUserTable=usmUserTable,
                         usmNoAuthProtocol=usmNoAuthProtocol, usmNoPrivProtocol=usmNoPrivProtocol,
                         usmUserEntry=usmUserEntry, usmUserAuthProtocol=usmUserAuthProtocol,
                         usmUserStatus=usmUserStatus, usmUserEngineID=usmUserEngineID,
                         usmUserAuthKeyChange=usmUserAuthKeyChange, usmDESPrivProtocol=usmDESPrivProtocol,
                         usmUserPrivProtocol=usmUserPrivProtocol, usmUserStorageType=usmUserStorageType,
                         usmUserPublic=usmUserPublic, usmStatsWrongDigests=usmStatsWrongDigests,
                         usmMIBGroups=usmMIBGroups, usmStats=usmStats,
                         usmStatsNotInTimeWindows=usmStatsNotInTimeWindows, PYSNMP_MODULE_ID=snmpUsmMIB,
                         usmMIBCompliance=usmMIBCompliance, usmStatsUnknownUserNames=usmStatsUnknownUserNames,
                         usmStatsUnknownEngineIDs=usmStatsUnknownEngineIDs, usmMIBCompliances=usmMIBCompliances,
                         KeyChange=KeyChange, usmMIBObjects=usmMIBObjects, usmUserName=usmUserName,
                         usmUserOwnAuthKeyChange=usmUserOwnAuthKeyChange, usmHMACMD5AuthProtocol=usmHMACMD5AuthProtocol,
                         usmMIBBasicGroup=usmMIBBasicGroup, usmStatsDecryptionErrors=usmStatsDecryptionErrors,
                         usmUserSpinLock=usmUserSpinLock, usmUserPrivKeyChange=usmUserPrivKeyChange)
