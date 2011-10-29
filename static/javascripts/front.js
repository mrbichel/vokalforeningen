(function() {
  var hsv2rgb, rgb2string;
  var __indexOf = Array.prototype.indexOf || function(item) {
    for (var i = 0, l = this.length; i < l; i++) {
      if (this[i] === item) return i;
    }
    return -1;
  };
  hsv2rgb = function(h, s, v) {
    var b, g, r, var_1, var_2, var_3, var_b, var_g, var_h, var_i, var_r;
    if (s === 0) {
      r = g = b = Math.round(v * 255);
    } else {
      var_h = h * 6;
      if (var_h === 6) {
        var_h = 0;
      }
      var_i = Math.floor(var_h);
      var_1 = v * (1 - s);
      var_2 = v * (1 - s * (var_h - var_i));
      var_3 = v * (1 - s * (1 - (var_h - var_i)));
      if (var_i === 0) {
        var_r = v;
        var_g = var_3;
        var_b = var_1;
      } else if (var_i === 1) {
        var_r = var_2;
        var_g = v;
        var_b = var_1;
      } else if (var_i === 2) {
        var_r = var_1;
        var_g = v;
        var_b = var_3;
      } else if (var_i === 3) {
        var_r = var_1;
        var_g = var_2;
        var_b = v;
      } else if (var_i === 4) {
        var_r = var_3;
        var_g = var_1;
        var_b = v;
      } else {
        var_r = v;
        var_g = var_1;
        var_b = var_2;
      }
      r = Math.round(var_r * 255);
      g = Math.round(var_g * 255);
      b = Math.round(var_b * 255);
    }
    return [r, g, b];
  };
  rgb2string = function(rgb) {
    return "rgb(" + rgb[0] + "," + rgb[1] + "," + rgb[2] + ")";
  };
  $(document).ready(function() {
    var rs, spacers;
    spacers = [];
    $("._rs, ._ls").each(function() {
      var hue, object, rgb;
      hue = Math.random();
      rgb = hsv2rgb(hue, 0.85, 0.3);
      object = {
        baseColor: rgb2string(rgb),
        highlightColor: rgb2string(hsv2rgb(hue, 0.95, 0.6)),
        el: $(this)
      };
      spacers.push(object);
      return $(this).css({
        backgroundColor: object.baseColor
      });
    });
    rs = [];
    $("#gallery img").css({
      opacity: "0.85"
    });
    return $("#gallery img").hover((function() {
      var n, r, _i, _len, _ref;
      rs = [];
      for (n = 0, _ref = spacers.length / 4; (0 <= _ref ? n <= _ref : n >= _ref); (0 <= _ref ? n += 1 : n -= 1)) {
        r = Math.floor(Math.random() * spacers.length);
        while (__indexOf.call(rs, r) >= 0) {
          r = Math.floor(Math.random() * spacers.length);
        }
        rs.push(r);
      }
      for (_i = 0, _len = rs.length; _i < _len; _i++) {
        r = rs[_i];
        spacers[r].el.animate({
          backgroundColor: spacers[r].highlightColor
        }, 200, function() {});
      }
      return $(this).css({
        opacity: "1"
      });
    }), function() {
      var r, _i, _len, _results;
      $(this).css({
        opacity: "0.85"
      });
      _results = [];
      for (_i = 0, _len = rs.length; _i < _len; _i++) {
        r = rs[_i];
        _results.push(spacers[r].el.animate({
          backgroundColor: spacers[r].baseColor
        }, 1200, function() {}));
      }
      return _results;
    });
  });
}).call(this);
