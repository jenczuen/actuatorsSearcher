
class Options:
    drive_shaft_options = {
        "Plain Shaft / Motor Standard",
        "Plain Shaft / Motor 180 Standard",
        "Double Plain Shaft"
    }

    all_mounting_kit_options = {
        "0-": "wihout",
        "A0": "SY563T",
        "A1": "SY873T",
        "A2": "SMx60 xx xxx 8 11 ...",
        "A3": "SMx82 xx xx 8 14 ...",
        "A4": "SMx100 xx xx 5 19...",
        "A7": "PS60",
        "C0": "LP050 / PV40-TA",
        "C1": "LP070 / PV60-TA"
    }

    mounting_kit_for_given_size = {
        25: {
            "0-": all_mounting_kit_options["0-"],
            "A0": all_mounting_kit_options["A0"],
            "A1": all_mounting_kit_options["A1"],
            "A2": all_mounting_kit_options["A2"],
            "C0": all_mounting_kit_options["C0"]
        },
        32: {
            "0-": all_mounting_kit_options["0-"],
            "A0": all_mounting_kit_options["A0"],
            "A1": all_mounting_kit_options["A1"],
            "A2": all_mounting_kit_options["A2"],
            "A3": all_mounting_kit_options["A3"],
            "A7": all_mounting_kit_options["A7"],
            "C0": all_mounting_kit_options["C0"],
            "C1": all_mounting_kit_options["C1"]
        },
        50: {
            "0-": all_mounting_kit_options["0-"],
            "A1": all_mounting_kit_options["A1"],
            "A3": all_mounting_kit_options["A3"],
            "A4": all_mounting_kit_options["A4"],
            "A7": all_mounting_kit_options["A7"],
            "C1": all_mounting_kit_options["C1"]
        }
    }

    profile_mounting_options = {
        "0": "without",
        "1": "Pair Type E1",
        "2": "1 Pair Type D1",
        "3": "1 Pair Type MAE",
        "4": "2 Pair Type 1",
        "5": "2 Pair Type D1",
        "6": "2 Pair Type MAE",
        "7": "3 Pair Type 1",
        "8": "3 Pair Type D1",
        "9": "3 Pair Type MAE",
        "K": "1 Pair Type E2",
        "L": "1 Pair Type E3",
        "M": "1 Pair Type E4",
        "N": "2 Pair Type E2",
        "P": "2 Pair Type E3",
        "Q": "2 Pair Type E4",
        "R": "3 Pair Type E2",
        "S": "3 Pair Type E3",
        "T": "3 Pair Type E4"
    }

    magnetic_sensors_options = {
        "0": "without",
        "1": "1 pc. RST-K 2NO / 5 m Cable",
        "2": "1 pc. RST-K 2NC / 5 m Cable",
        "3": "2 pc. RST-K 2NC / 5 m Cable",
        "4": "2 pc. RST-K 2NC, 1 pc. RST-K 2NO / 5 m Cable",
        "5": "1 pc. RST-S 2NO / M8 plug",
        "6": "1 pc. RST-S 2NC / M8 plug",
        "7": "2 pc. RST-S 2NC / M8 plug",
        "8": "2 pc. RST-S 2NC, 1 pc. RST-S 2NO / M8 plug",
        "A": "1 pc. EST-S NPN / M8 plug",
        "B": "2 pc. EST-S NPN / M8 plug",
        "C": "3 pc. EST-S NPN / M8 plug",
        "D": "1 pc. EST-S PNP / M8 plug",
        "E": "2 pc. EST-S PNP / M8 plug",
        "F": "3 pc. EST-S PNP / M8 plug"
    }