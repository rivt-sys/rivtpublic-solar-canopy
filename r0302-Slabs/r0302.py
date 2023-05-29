# %%
import rivtlib.rv_lib as rv

rv.D(" ", "default", "Carport Wind Model", "1")

rv.I("""[01] Carport Unit Loads and Weight

    Roof unit dead loads [t]_

    [literal]_                                        
    ==========  =======  =========  =================================
    variable      value    [value]  description
    ==========  =======  =========  =================================
    ld1         2.0 psf  0.096 KPa  Urethane foam (4 inch thick)
    ld2         1.0 psf  0.048 KPa  Three-ply roofing
    ld3         5.0 psf  0.239 KPa  Doug Fir decking 2-in.
    ld4         1.0 psf  0.048 KPa  Doug Fir beams 4x12 at 12 ft o.c.
    ==========  =======  =========  =================================

     """)

rv.V(""" Carport Weight

    Carport Geometry [t]_
    cp_width = 22.75        | FT,M | carport width
    cp_length = 19.5        | FT,M | carport length
    roofdl1 = .009          | KSF, KPA | unit load
    newfnd =  .15           | KIPS, KN | new foundations

    Weight of carport [e]_
    cp_wt = (newfnd * 6) + (cp_width * cp_length * roofdl1) | KIPS, KN             
    """)

rv.V("""[02] Wind loads

    Wind loads are calculated using a MeccaWind model. Model parameters and
    output are provided in Section 3.

    Wind Force Values [t]_
    uplift_max = 2.8        | KIPS, KN | nominal maximum wind uplift

    Uplift DC ratio [e]_
    dc1 = uplift_max / (.9*cp_wt)          | DC


    Mecca Wind Model Results [t]_
    || text | wind_pressures3.html | html
     """)

rv.V("""[03] MeccaWind Output

    Mecca Wind Model Results [t]_
    || text | wind_pressures3.html | html

    ---------------------------------

    || image | fig2.png,fig3.png | 30,40
    Wind load geometry - 90 deg [f]_
    Wind load orientation - 180 deg [f]_
    
    || image | winda180.png,windb180.png | 45,45
    Positive wind load pressures [f]_
    Negative wind load pressures [f]_
     """)

# %%
