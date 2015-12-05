#!/usr/bin/python3

def make(n):
    fname = "Pin_Header_Straight_1x{:02d}_1_27mm.kicad_mod".format(n)

    print("Making: " + fname)

    d = {}
    d['npins'] = n

    # first pad is rectangular
    d['pads'] = "(pad 1 thru_hole rect (at 0 0) (size 1.143 1.143) (drill 0.7)\
     (layers *.Cu *.Mask F.SilkS))\n"
    # template for other pads
    pad_t = "  (pad {} thru_hole oval (at 0 {}) (size 1.143 0.889) (drill 0.7) (layers *.Cu *.Mask F.SilkS))"

    pitch = 1.27
    # create pads from template
    d['pads'] += '\n'.join(pad_t.format(i+1, i*pitch) for i in range(1,n))


    d['cy_end'] = (n - 1) * pitch + 1 # courtyard bottom
    d['ss_y1'] = pitch/2.0            # silkscreen -bottom part- top
    d['ss_y2'] = pitch/2.0 + pitch*(n-1) + 0.1 # silkscreen -bottom part- bottom

    file_t = """(module Pin_Header_Straight_1x{npins:02d}_1_27mm (layer F.Cu) (tedit 54EA090C)
  (descr "1x{npins:02d} through hole pin header 1.27mm pitch")
  (tags "pin header")
  (fp_text reference REF** (at 0 -5.1) (layer F.SilkS)
    (effects (font (size 1 1) (thickness 0.15)))
  )
  (fp_text value Pin_Header_Straight_1x{npins:02d}_1_27mm (at 0 -3.1) (layer F.Fab)
    (effects (font (size 1 1) (thickness 0.15)))
  )
  (fp_line (start -1.2 -1.2) (end -1.2 {cy_end}) (layer F.CrtYd) (width 0.05))
  (fp_line (start 1.2 -1.2) (end 1.2 {cy_end}) (layer F.CrtYd) (width 0.05))
  (fp_line (start -1.2 -1.2) (end 1.2 -1.2) (layer F.CrtYd) (width 0.05))
  (fp_line (start -1.2 {cy_end}) (end 1.2 {cy_end}) (layer F.CrtYd) (width 0.05))

  (fp_line (start -1.0 0) (end -1.0 -1.0) (layer F.SilkS) (width 0.15))
  (fp_line (start -1.0 -1.0) (end 1.0 -1.0) (layer F.SilkS) (width 0.15))
  (fp_line (start 1.0 -1.0) (end 1.0 0) (layer F.SilkS) (width 0.15))

  (fp_line (start -0.9 {ss_y1}) (end -1 {ss_y1}) (layer F.SilkS) (width 0.15))
  (fp_line (start 0.9 {ss_y1}) (end 1 {ss_y1}) (layer F.SilkS) (width 0.15))

  (fp_line (start 1 {ss_y1}) (end 1 {ss_y2}) (layer F.SilkS) (width 0.15))
  (fp_line (start -1 {ss_y1}) (end -1 {ss_y2}) (layer F.SilkS) (width 0.15))
  (fp_line (start -1 {ss_y2}) (end 1 {ss_y2}) (layer F.SilkS) (width 0.15))
  {pads}
)"""

    result = file_t.format(**d)

    with open(fname, 'w') as f:
        f.write(result)
        print("Done: "+fname)

def make_all():
    for i in range(1,40+1):
        make(i)
    print("Done.")

if __name__ == "__main__":
    make_all()
