
2023-06-19 00:00
-------
# Overview and Codes

This report covers the structural design of a residential solar canopy
located in Larkspur, California. It includes the design of a concrete slab
and stem wall foundation, a welded steel tube frame, and solar panel clips.

(... for project data - see report output ...)


## 0101-[1] Governing Codes


<img src=data/fig1.png width=15% alt=data/fig1.png
[1] Fig. 01

<img src=data/fig2.png width=40% alt=data/fig2.png
[1] Fig. 02

Building Codes and Jurisdiction
- City of Larkspur, California
- 2019 California Building Code [CBC]
- 2019 California Residential Code [CRC]

The canopy is designed for compliance with the requirements of the CBC.

[1] Table 01
| Loading                                             | ASCE-7    | 2016 |
| --------------------------------------------------- | --------- | ---- |
| Concrete                                            | ACI-318   | 2014 |
| Wood-National Design Specifications                 | AWC-NDS   | 2018 |
| Wood-Special Design Provisions for Wind and Seismic | AWC-SDPWS | 2015 |
| Wood Frame Construction Manual                      | AWC-WFCM  | 2018 |

Basic loads and load combinations are derived from the California Building
and Residential Codes.

[1] Table 02
| D   | Dead load                 | See IBC 1606 and Chapter 3 of this
| publication |
| ----------- |  ||
| E           | Combined effect of horizontal and |
vertical earthquake-induced forces
as defined in ASCE/SEI 12.4.2                           | See IBC 1613, ASCE/SEI 12.4.2 and
Chapter 6 of this publication                                     |
| Em  | Maximum seismic load effect of
horizontal and vertical forces as
set forth in ASCE/SEI 12.4.3                           | See IBC 1613, ASCE/SEI 12.4.3 and
Chapter 6 of this publication                                     |
| H   | Load due to lateral earth
pressures, ground water pressure or
pressure of bulk materials                           | See IBC 1610 for soil lateral loads |
| L   | Live load, except roof live load,
including any permitted live load
reduction                           | See IBC 1607 and Chapter 3 of this
publication                                     |
| Li  | Roof live load including any
permitted live load reduction                           | See IBC 1607 and Chapter 3 of this
publication                                     |
| R   | Rain load                 | See IBC 1611 and Chapter 3 of this
publication                                     |
| W   | Load due to wind pressure | See IBC 1609 and Chapter 5 of this
publication                                     |

[1] Table 03
| Equation 16-1 | 1.4(D +F)                                             |
| ------------- | ----------------------------------------------------- |
| Equation 16-2 | 1.2(D + F) + l.6(L + H) + 0.5(L                       |
| Equation 16-3 | 1.2(D + F) + l.6(Lr or S or R) + l.6H + (f1L or 0.5W) |
| Equation 16-4 | 1.2(D + F) + 1.0W + f1L +1.6H + 0.5(Lr or S or R)     |
| Equation 16-5 | 1.2(D + F) + 1.0E + f1L + l.6H + f2S                  |
| Equation 16-6 | 0.9D+ l.0W+ l.6H                                      |
| Equation 16-7 | 0.9(D + F) + 1.0E+ l.6H                               |


## 0101-[2] Gravity Loads and Seismic Mass


Some filler text
