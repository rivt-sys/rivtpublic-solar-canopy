
--------------------------------------------------------------------------------
 Overview                                                           [0101] - 1
--------------------------------------------------------------------------------
========  =============  =================  =============================  =====
  Type      No./Date           Name                    Address               Zip
========  =============  =================  =============================  =====
 Client       C001         Bryna Holland       15 Blanca Drive, Novato     94947
Project       P010       Residence Remodel  55 Loring Avenue, Mill Valley  94941
Drawings  Dec. 1 , 2020   PR-01 to PR-11    55 Loring Avenue, Mill Valley  94941
========  =============  =================  =============================  =====--------------------------------------------------------------------------------
 Governing Codes                                                    [0101] - 2
--------------------------------------------------------------------------------
Figure path: rivtlocal-solar-canopy\rv01-loads\fig1.png
Fig. 00 - Wind load 1                                                  02 - F00
Figure path: rivtlocal-solar-canopy\rv01-loads\fig2.png
Fig. 01 - Wind load 2                                                  02 - F01
Table 00 - Standards                                                    02 - T00
===================================================  =========  ======
Loading                                              ASCE-7       2016
===================================================  =========  ======
Concrete                                             ACI-318      2014
Wood-National Design Specifications                  AWC-NDS      2018
Wood-Special Design Provisions for Wind and Seismic  AWC-SDPWS    2015
Wood Frame Construction Manual                       AWC-WFCM     2018
===================================================  =========  ======Table 01 - Load Types                                                   02 - T01
===  ===================================  ====================================
D    Dead load                            See IBC 1606 and Chapter 3 of this
                                          publication
===  ===================================  ====================================
E    Combined effect of horizontal and    See IBC 1613, ASCE/SEI 12.4.2 and
     vertical earthquake-induced forces   Chapter 6 of this publication
     as defined in ASCE/SEI 12.4.2
Em   Maximum seismic load effect of       See IBC 1613, ASCE/SEI 12.4.3 and
     horizontal and vertical forces as    Chapter 6 of this publication
     set forth in ASCE/SEI 12.4.3
H    Load due to lateral earth            See IBC 1610 for soil lateral loads
     pressures, ground water pressure or
     pressure of bulk materials
L    Live load, except roof live load,    See IBC 1607 and Chapter 3 of this
     including any permitted live load    publication
     reduction
Li   Roof live load including any         See IBC 1607 and Chapter 3 of this
     permitted live load reduction        publication
R    Rain load                            See IBC 1611 and Chapter 3 of this
                                          publication
W    Load due to wind pressure            See IBC 1609 and Chapter 5 of this
                                          publication
===  ===================================  ====================================Table 02 - Load Combinations                                            02 - T02
===============  =====================================================
 Equation 16-1                         1.4(D +F)
===============  =====================================================
 Equation 16-2              1.2(D + F) + l.6(L + H) + 0.5(L
 Equation 16-3   1.2(D + F) + l.6(Lr or S or R) + l.6H + (f1L or 0.5W)
 Equation 16-4     1.2(D + F) + 1.0W + f1L +1.6H + 0.5(Lr or S or R)
 Equation 16-5           1.2(D + F) + 1.0E + f1L + l.6H + f2S
 Equation 16-6                     0.9D+ l.0W+ l.6H
 Equation 16-7                  0.9(D + F) + 1.0E+ l.6H
===============  =====================================================--------------------------------------------------------------------------------
 Gravity Loads and Seismic Mass                                     [0101] - 3
--------------------------------------------------------------------------------
Table 03 - Roof unit dead loads                                         03 - T03
==========  =======  =========  =================================
variable      value    [value]  description
==========  =======  =========  =================================
ld1         2.0 psf   0.10 KPa  Urethane foam (4 inch thick)
ld2         1.0 psf   0.05 KPa  Three-ply roofing
ld3         5.0 psf   0.24 KPa  Doug Fir decking 2-in.
ld4         1.0 psf   0.05 KPa  Doug Fir beams 4x12 at 12 ft o.c.
-                 -          -  Total
roofdl1     9.0 psf   0.43 KPa  Total roof unit load
==========  =======  =========  =================================Table 04 - Floor unit dead loads                                        03 - T04
==========  ========  =========  ==========================
variable       value    [value]  description
==========  ========  =========  ==========================
ld1          3.0 psf   0.14 KPa  3/4 in. hardwood flooring
ld2          2.0 psf   0.10 KPa  1/2 in. plywood subfloor
ld3          4.0 psf   0.19 KPa  2x10 joists at 16 in. o.c.
ld4          1.5 psf   0.07 KPa  fixtures
-                  -          -  Total
floordl1    10.5 psf   0.50 KPa  Total floor unit load
==========  ========  =========  ==========================Table 05 - Interior wall unit dead loads                                03 - T05
==========  =======  =========  =============================
variable      value    [value]  description
==========  =======  =========  =============================
ld1         5.5 psf   0.26 KPa  5/8" sheet rock (2)
ld2           2 psf   0.10 KPa  2x4 studs at 16" o.c.
ld3         1.5 psf   0.07 KPa  fixtures
-                 -          -  Total
intwalldl1    9 psf   0.43 KPa  Total interior wall unit load
==========  =======  =========  =============================Table 06 - Exterior wall unit dead loads                                03 - T06
==========  =======  =========  =============================
variable      value    [value]  description
==========  =======  =========  =============================
ld1         2.0 psf   0.10 KPa  1/2 in plywood sheathing
ld2         2.0 psf   0.10 KPa  2x4 studs at 16 in o.c.
ld3         3.0 psf   0.14 KPa  5/8 in sheet rock
ld4         1.5 psf   0.07 KPa  fixtures
-                 -          -  Total
extwalldl1  8.5 psf   0.41 KPa  Total exterior wall unit load
==========  =======  =========  =============================Table 07 - Areas                                                        03 - T07
==========  ==========  =========  ======================
variable         value    [value]  description
==========  ==========  =========  ======================
arearf1     1700.00 sf  157.94 SM  roof area
areaflr1    1200.00 sf  111.48 SM  floor area
htwall1        9.00 ft     2.74 m  wall height
lenwall1     110.00 ft    33.53 m  interior wall length
lenwall2     155.00 ft    47.24 m  exterior wall length 2
==========  ==========  =========  ======================

Equ. 01 - Roof weight                                                   03 - E01

rfwt₁ = arearf₁⋅roofdl₁

15.30 kip = 1700.00 sf⋅9.00 psf



Equ. 02 - Floor weight                                                  03 - E02

flrwt₁ = areaflr₁⋅floordl₁

12.60 kip = 10.50 psf⋅1200.00 sf



Equ. 03 - Partition weight                                              03 - E03

partwt₁ = htwall₁⋅intwalldl₁⋅lenwall₁

8.91 kip = 110.00 ft⋅9.00 ft⋅9.00 psf



Equ. 04 - Exterior wall weight                                          03 - E04

exwallwt₁ = extwalldl₁⋅htwall₁⋅lenwall₂

11.86 kip = 155.00 ft⋅8.50 psf⋅9.00 ft



Equ. 05 - Total building weight                                         03 - E05

totwt₁ = exwallwt₁ + flrwt₁ + partwt₁ + rfwt₁

48.67 kip = 11857.50 lbs + 12600.00 lbs + 15300.00 lbs + 8910.00 lbs



Table 08 - Weights                                                      03 - T08
==========  =========  =========  ===========================
variable        value    [value]  description [eq. number]
==========  =========  =========  ===========================
rfwt1       15.30 kip   68.06 KN  Roof weight  [01]
flrwt1      12.60 kip   56.05 KN  Floor weight  [02]
partwt1      8.91 kip   39.63 KN  Partition weight  [03]
exwallwt1   11.86 kip   52.74 KN  Exterior wall weight  [04]
totwt1      48.67 kip  216.48 KN  Total building weight  [05]
==========  =========  =========  ===========================

--------------------------------------------------------------------------------
 Material Densities and Seismic Models                              [0101] - 4
--------------------------------------------------------------------------------
Equ. 06 - Effective model floor load                                    04 - E06

          flrwt₁ + partwt₁
eflrdl₁ = ────────────────
              areaflr₁    

            12600.00 lbs + 8910.00 lbs
17.93 psf = ──────────────────────────
                    1200.00 sf        



Equ. 07 - Effective model floor density                                 04 - E07

            eflrdl₁
eflrdens₁ = ───────
             0.5⋅IN

           17.93 lbs/sf
0.25 pci = ────────────
              0.5⋅in   



Equ. 08 - Effective model roof density                                  04 - E08

           roofdl₁
erfdens₁ = ───────
            1.5⋅IN

           9.00 psf
0.04 pci = ────────
            1.5⋅in 



Equ. 09 - Effective model wall density                                  04 - E09

             extwalldl₁
ewalldens₁ = ──────────
               0.5⋅IN  

           8.50 psf
0.12 pci = ────────
            0.5⋅in 



Table 09 - Model loads                                                  04 - T09
==========  =========  ==========  ===================================
variable        value     [value]  description [eq. number]
==========  =========  ==========  ===================================
eflrdl1     17.93 psf    0.86 KPa  Effective model floor load   [06]
eflrdens1    0.25 pci  67.58 KNcM  Effective model floor density  [07]
erfdens1     0.04 pci  11.31 KNcM  Effective model roof density  [08]
ewalldens1   0.12 pci  32.05 KNcM  Effective model wall density  [09]
==========  =========  ==========  ===================================

--------------------------------------------------------------------------------
 Abbreviations and References                                       [0101] - 5
--------------------------------------------------------------------------------
                                  References                                    
    ACI 
    American Concrete Institute 
    38800 Country Club Drive 
    Farmington Hills, MI 48331 
    318—14 

    AISC 
    American Institute of Steel 
    130 East Randolph Street, Suite 2000 
    Chicago, IL 60601-6219 
    ANSI/AISC 341—16 
    Seismic Provisions for Structural Steel Buildings 

    AISI 
    American Iron and Steel Institute 
    25 Massachusetts Avenue, NW Suite 800 
    Washington, DC 20001 
    AISI S100—16 
    North American Specification for the Design of Cold-formed 
    Steel Structural Members, 2016 

    ASCE/SEI 
    American Society of Civil Engineers 
    Structural Engineering Institute 
    1801 Alexander Bell Drive 
    Reston, VA 20191-4400 
    7—16 Minimum Design Loads and Associated Criteria for 
    Buildings and Other Structures with Supplement No. 1 

    AWC 
    American Wood Council 
    222 Catoctin Circle SE, Suite 201 
    Leesburg, VA 20175 
    ANSI/AWC NDS—2018 
    National Design Specification (NDS) for 
    Wood Construction—with 2018 NDS Supplement 
    ANSI/AWC SDPWS—2015 
    Special Design Provisions for Wind and Seismic 

    CBC
    International Code Council
    500 New Jersey Avenue, NW
    6th Floor, Washington, DC 20001
    California Building Standards Commission
    2525 Natomas Park Dr # 130, Sacramento, CA 95833
    California Building Code 
    Part 2 of Title 24, 2019 Edition

    CRC
    International Code Council
    500 New Jersey Avenue, NW
    6th Floor, Washington, DC 20001
    California Building Standards Commission
    2525 Natomas Park Dr # 130, Sacramento, CA 95833
    California Residential Code 
    Part 2.5 of Title 24, 2019 Edition                                   Drawings                                     
    
    55 LORING - RESIDENCE REMODEL AND SEISMIC STRENGTHENING 
    
    PR.01: COVER AND INDEX
    PR.02: PROJECT SCOPE
    PR.03: GENERAL NOTES, CONTRACTORS
    PR.04: SITE PLAN
    PR.05: PLANS
    PR.06: ELEVATIONS
    PR.07: KITCHEN AND BATH REMODEL
    PR.08: MASTER BATH, CLOSET, LAUNDRY
    PR.09: RESIDENCE STRENGTHENING
    PR.10: CARPORT STRENGTHENING
    PR.11: SITE IMPROVEMENTS                             Abbreviations - Terms                              
0.2in-0.3in4cm\=\
ASD\      Allowable Stress Design
ACI\      American Concrete Institute
AISC\     American Institute of Steel Construction
AISI\     American Iron and Steel Institute
ASTM\     American Society for Testing and Materials
AWS\      American Welding Society
AB\       Anchor Bolt
BDRY\     Boundry
CBC\      Califiornia Building Code
CRC\      Califiornia Residential Code
CIP\      Cast-In-Place
CLR\      Clear
CONC\     Concrete
CMU\      Concrete Masonry Unit
CRSI\     Concrete Reinforcing Steel Institute
CONST JT\ Construction Joint
CONT\     Continuous
CJ\       Control Joint
D-C\      Demand-Capacity (ratio)
DIA\      Diameter
DIM\      Dimension
EA\       Each
EF\       Each Face
EJ\       Expansion Joint
ES\       Each Side
EW\       Each Way
EXP Bolt\ Expansion Bolt
EXP JT\   Expansion Joint
FTG\      Footing
FND\      Foundation
GALV\     Galvanized
GA\       Gauge
GR\       Grade
HT\       Height
IN\       Inch
ID\       Inside Diameter
ICBO\     International Conference of Building Officials
K\        Kip (1000 Pounds)
LWC\      Light Weight Concrete
LRFD\     Load and Resistance Factor Design
NWC\      Normal Weight Concrete
NIC\      Not in Contract
OC\       On Center
OD\       Outside Diameter
OPNG\     Opening
PVC\      Polyvinyl Chloride
PSF\      Pounds per Square Foot
PSI\      Pounds per Square Inch
R\        Radius
REINF\    Reinforced
SIM\      Similar
SOG\      Slab on Grade
SL\       Splice Length
SQ\       Square
STD\      Standard
SDI\      Steel Deck Institute
SF\       Step Footing or Square Foot
SYM\      Symmetrical
THK\      Thick or Thickness
T \& B\   Top and Bottom
T \& G\   Tongue and Groove
TOC\      Top of Concrete
TOF\      Top of Foundation
TOS\      Top of Steel
TOW\      Top of Wall
TYP\      Typical
UNO\      Unless Noted Otherwise
WWF\      Welded Wire Fabric
W/\       With
WP\       Working Point
                             Abbreviations - Math                               
-.4inD& = dead load
L& = live load
D_m& = module dead load
E& = earthquake load
F_a& = acceleration site coefficient
F_v& = velocity site coefficient
F_N& = normal wind force
GC_M_s& = net moment static coefficient
GC_M_d& = net moment dynamic coefficient
GC_M& = net moment coefficient
GC_P& = net pressure coefficient
GC_P_s& = net static pressure coefficient
GC_P_d& = net dynamic pressure coefficient
k_1& = hazard coefficient
k_2& = terrain and structure coefficient
k_3& = topography coefficient
Kzt& = topographic Factor
K_z& = velocity pressure exposure coefficient
MRI& = mean return interval
p_d& = net design wind pressure on module - Pa
SDOF& = single degree of freedom
S_s& = short period mapped acceleration
S_D_S& = site design response acceleration
S_1& = 1 second period mapped acceleration
S_M_S& = short period parameter
S_M_1& = 1 second period parameter
T& = fundamental period of structure
M_t_o_r& = wind moment about panel center 
T_0& = short period spectral cap 
T_S& = long period spectral cap
V_b& = basic wind speed
V_B& = seismic design base shear
W& = wind load
W& = seismic weight of structure 
