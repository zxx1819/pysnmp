# PySNMP SMI module. Autogenerated from smidump -f python SNMP-USM-AES-MIB
# by libsmi2pysnmp-0.0.8-alpha at Tue Feb  5 21:34:16 2008,
# Python version (2, 4, 4, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( snmpPrivProtocols, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "snmpPrivProtocols")
( Bits, Integer32, ModuleIdentity, MibIdentifier, ObjectIdentity, TimeTicks, snmpModules, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "TimeTicks", "snmpModules")

# Objects

usmAesCfb128Protocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 2, 4))
if mibBuilder.loadTexts: usmAesCfb128Protocol.setDescription("The CFB128-AES-128 Privacy Protocol.")
snmpUsmAesMIB = ModuleIdentity((1, 3, 6, 1, 6, 3, 20)).setRevisions(("2004-06-14 00:00",))
if mibBuilder.loadTexts: snmpUsmAesMIB.setOrganization("IETF")
if mibBuilder.loadTexts: snmpUsmAesMIB.setContactInfo("Uri Blumenthal\nLucent Technologies / Bell Labs\n67 Whippany Rd.\n14D-318\nWhippany, NJ  07981, USA\n973-386-2163\nuri@bell-labs.com\n\nFabio Maino\nAndiamo Systems, Inc.\n375 East Tasman Drive\nSan Jose, CA  95134, USA\n408-853-7530\nfmaino@andiamo.com\n\nKeith McCloghrie\nCisco Systems, Inc.\n170 West Tasman Drive\nSan Jose, CA  95134-1706, USA\n\n408-526-5260\nkzm@cisco.com")
if mibBuilder.loadTexts: snmpUsmAesMIB.setDescription("Definitions of Object Identities needed for\nthe use of AES by SNMP's User-based Security\nModel.\n\nCopyright (C) The Internet Society (2004).\n\nThis version of this MIB module is part of RFC 3826;\nsee the RFC itself for full legal notices.\nSupplementary information may be available on\nhttp://www.ietf.org/copyrights/ianamib.html.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("SNMP-USM-AES-MIB", PYSNMP_MODULE_ID=snmpUsmAesMIB)

# Objects
mibBuilder.exportSymbols("SNMP-USM-AES-MIB", usmAesCfb128Protocol=usmAesCfb128Protocol, snmpUsmAesMIB=snmpUsmAesMIB)

