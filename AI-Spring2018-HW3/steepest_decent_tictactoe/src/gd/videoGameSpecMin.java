/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package gd;

import java.util.Arrays;
import java.util.HashMap;

/**
 *
 * @author Warren MacEvoy
 *
 * Silly minimization example based on Dr. Strange movie. Assuming you must have
 * a positive number of jokes and between 0 and 2 fights, maximize the appeal of
 * the movie.
 */
public class videoGameSpecMin implements RealMin {

    double[] values = new double[2];
    private static final String[] names = new String[]{"strength", "speed"};
    private static final HashMap< String, Integer> indexes = new HashMap< String, Integer>();

    static {
        for (int i = 0; i < names.length; ++i) {
            indexes.put(names[i], i);
        }
    }
    public static final int ISTRENGTH = indexes.get("strength");
    public static final int ISPEED = indexes.get("speed");

    @Override
    public int getRealParameterSize() {
        return names.length;
    }

    @Override
    public String getRealParameterName(int i) {
        return names[i];
    }

    @Override
    public int getRealParameterIndex(String name) {
        return indexes.get(name);
    }

    @Override
    public double getRealParameterValue(int index) {
        return values[index];
    }

    @Override
    public void setRealParameterValue(int index, double value) {
        values[index] = value;
    }

    public videoGameSpecMin() {
    }

    public videoGameSpecMin(videoGameSpecMin copy) {
        System.arraycopy(copy.values, 0, copy.values, 0, values.length);
    }

    @Override
    public RealMin copy() {
        return new videoGameSpecMin(this);
    }

    @Override
    public double getValue() {
        double strength = values[ISTRENGTH];
        double speed = values[ISPEED];
        double d2 = 0;
        double weight = 250;
        boolean constrained = true;
        if (constrained) {

            if (strength < 0) {
                d2 += strength * strength;
                strength = 0;
            }

            if (speed < 0) {
                d2 += speed * speed;
                speed = 0;
            }
            if (strength > 450) {
                d2 += (strength - 450) * (strength - 450);
                strength = 450;
            }
            if (speed > 450) {
                d2 += (speed - 450) * (speed - 450);
                speed = 450;
            }
        }
        return Math.pow((strength - speed)+weight, 2) + Math.pow((speed-strength)+weight/2, 2) + d2;
    }
}
