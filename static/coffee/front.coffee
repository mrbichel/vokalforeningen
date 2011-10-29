hsv2rgb = (h,s,v) ->
    # hsv values = 0 - 1, rgb values = 0 - 255

    if s is 0
      r = g = b = Math.round(v*255)
    else
      #h must be < 1
      var_h = h * 6
      if var_h is 6
        var_h = 0
      #Or ... var_i = floor( var_h )
      var_i = Math.floor( var_h )
      var_1 = v*(1-s)
      var_2 = v*(1-s*(var_h-var_i))
      var_3 = v*(1-s*(1-(var_h-var_i)))
      if var_i is 0
        var_r = v
        var_g = var_3
        var_b = var_1
      else if var_i is 1
        var_r = var_2
        var_g = v
        var_b = var_1
      else if var_i is 2
        var_r = var_1
        var_g = v
        var_b = var_3
      else if var_i is 3
        var_r = var_1
        var_g = var_2
        var_b = v
      else if var_i is 4
        var_r = var_3
        var_g = var_1
        var_b = v
      else
        var_r = v
        var_g = var_1
        var_b = var_2

      #rgb results = 0 ÷ 255
      r = Math.round(var_r * 255)
      g = Math.round(var_g * 255)
      b = Math.round(var_b * 255)

    return [r,g,b]

rgb2string = (rgb) ->
    return "rgb(" + rgb[0] + "," + rgb[1] + "," + rgb[2] + ")"





$(document).ready ->

    spacers = []

    $("._rs, ._ls").each ->
        hue = Math.random()
        rgb = hsv2rgb(hue, 0.85, 0.3)
        
        object =
            baseColor: rgb2string(rgb)
            highlightColor: rgb2string(hsv2rgb(hue, 0.95, 0.6))
            el: $(this)

        spacers.push object

        $(this).css
            backgroundColor: object.baseColor

    rs = []


    $("#gallery img").css
        opacity: "0.85"


    $("#gallery img").hover (->
        rs = []
        for n in [0..spacers.length/4]
            r = Math.floor((Math.random()*spacers.length))
            while r in rs
                r = Math.floor((Math.random()*spacers.length))
            rs.push r

        for r in rs
            spacers[r].el.animate
                backgroundColor: spacers[r].highlightColor
            , 200, ->

        $(this).css
            opacity: "1"

    ), ->
        $(this).css
            opacity: "0.85"

        for r in rs
            spacers[r].el.animate
                backgroundColor: spacers[r].baseColor
            , 1200, ->
                


