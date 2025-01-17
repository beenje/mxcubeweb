test_sample_1 = {
    "code": "matr1_1",
    "checked": True,
    "sampleName": "Sample-101",
    "sampleID": "1:01",
    "tasks": [],
    "location": "1:1",
    "defaultPrefix": "local-user",
    "type": "Sample",
}

test_sample_5 = {
    "code": "matr1_5",
    "checked": True,
    "sampleName": "Sample-105",
    "sampleID": "1:05",
    "tasks": [],
    "location": "1:5",
    "defaultPrefix": "local-user",
    "type": "Sample",
}

test_sample_6 = {
    "code": "matr1_6",
    "checked": True,
    "sampleName": "Sample-106",
    "sampleID": "1:06",
    "tasks": [],
    "location": "1:6",
    "defaultPrefix": "local-user",
    "type": "Sample",
}

test_task = {
    "checked": True,
    "code": "matr1_5",
    "defaultPrefix": "local-user",
    "defaultSubDir": "Sample-1-05/",
    "loadable": True,
    "location": "1:05",
    "proteinAcronym": "",
    "queueID": 1,
    "sampleID": "1:05",
    "sampleName": "Sample-1:05",
    "state": 0,
    "tasks": [
        {
            "type": "DataCollection",
            "label": "Data Collection",
            "state": 0,
            "sampleID": "1:05",
            "sampleQueueID": 1,
            "parameters": {
                "detector_mode": [],
                "energy": 12,
                "exp_time": 1,
                "first_image": 1,
                "helical": False,
                "inverse_beam": False,
                "kappa": 0,
                "kappa_phi": 0,
                "mesh": False,
                "num_images": 1,
                "num_passes": 1,
                "osc_range": 1,
                "osc_start": 90,
                "overlap": 0,
                "prefixTemplate": None,
                "resolution": 3,
                "shutterless": True,
                "skip_existing_images": False,
                "subDirTemplate": None,
                "take_dark_current": 1,
                "take_snapshots": 1,
                "transmission": 100,
                "prefix": "local-user",
                "path": "",
                "subdir": "Sample-1-05/",
                "shape": -1,
                "beam_size": 5,
                "type": "DataCollection",
                "label": "Data Collection",
            },
            "checked": True,
        }
    ],
    "type": "Sample",
}

test_edit_task = {
    "checked": True,
    "label": "Data Collection",
    "limsResultData": {
        "limsTaskLink": "https://your.limsresults.org/ispyb/user/viewResults.do?reqCode=display&dataCollectionId=null"
    },
    "parameters": {
        "detector_mode": [],
        "energy": 12,
        "exp_time": 1,
        "fileName": None,
        "first_image": 1,
        "fullPath": None,
        "helical": False,
        "inverse_beam": False,
        "kappa": 0,
        "kappa_phi": 0,
        "mesh": False,
        "num_images": 1,
        "num_passes": 1,
        "osc_range": 1,
        "osc_start": 0,
        "overlap": 0,
        "path": None,
        "prefix": "idtest0",
        "resolution": 3,
        "run_number": 1,
        "shape": -1,
        "shutterless": True,
        "snapshot": None,
        "subdir": "Sample-1-01/",
        "transmission": 100,
        "beam_size": 5,
        "type": "DataCollection",
        "label": "Data Collection",
    },
    "queueID": 3,
    "sampleID": "1:01",
    "sampleQueueID": 1,
    "state": 0,
    "taskIndex": 0,
    "type": "DataCollection",
}

default_dc_params = {
    "acq_parameters": {
        "detector_mode": 1,
        "exp_time": 0.02,
        "first_image": 1,
        "helical": False,
        "inverse_beam": False,
        "kappa": 11.0,
        "kappa_phi": 22.0,
        "mesh": False,
        "num_images": 1,
        "num_passes": 1,
        "osc_range": 0.1,
        "overlap": 0,
        "prefixTemplate": "{PREFIX}_{POSITION}",
        "shutterless": True,
        "skip_existing_images": False,
        "subDirTemplate": "{ACRONYM}/{ACRONYM}-{NAME}",
        "take_dark_current": True,
        "take_snapshots": True,
    },
    "limits": {
        "exposure_time": [0.02, 1000],
        "kappa": [-5.0, 240.0],
        "number_of_images": [1, 99999],
        "osc_range": [-10000, 10000],
    },
}

default_char_acq_params = {
    "acq_parameters": {
        "account_rad_damage": True,
        "aimed_completness": 0.99,
        "aimed_i_sigma": 1.0,
        "aimed_multiplicity": 0,
        "auto_res": True,
        "beta": 1,
        "burn_osc_interval": 3,
        "burn_osc_start": 0.0,
        "detector_mode": 1,
        "determine_rad_params": False,
        "exp_time": 0.05,
        "experiment_type": 7,
        "first_image": 1,
        "gamma": 0.06,
        "induce_burn": False,
        "inverse_beam": False,
        "kappa": 11.0,
        "kappa_phi": 22.0,
        "low_res_pass_strat": False,
        "max_crystal_vdim": 0.05,
        "max_crystal_vphi": 90,
        "min_crystal_vdim": 0.05,
        "min_crystal_vphi": 0.0,
        "min_dose": 30.0,
        "min_time": 0.0,
        "num_images": 4,
        "num_passes": 1,
        "opt_sad": False,
        "osc_range": 1,
        "overlap": -89,
        "permitted_phi_end": 360,
        "permitted_phi_start": 0.0,
        "prefixTemplate": "{PREFIX}_{POSITION}",
        "rad_suscept": 1.0,
        "sad_res": 0.5,
        "shutterless": False,
        "skip_existing_images": False,
        "space_group": "",
        "strategy_complexity": 0,
        "subDirTemplate": "{ACRONYM}/{ACRONYM}-{NAME}",
        "take_dark_current": True,
        "take_snapshots": True,
        "use_aimed_multiplicity": False,
        "use_aimed_resolution": False,
        "use_min_dose": True,
        "use_min_time": False,
        "use_permitted_rotation": False,
    }
}

default_char_params = {
    "account_rad_damage": True,
    "aimed_completness": 0.99,
    "aimed_i_sigma": 1.0,
    "aimed_multiplicity": 0,
    "auto_res": True,
    "beta": 1,
    "burn_osc_interval": 3,
    "burn_osc_start": 0.0,
    "determine_rad_params": False,
    "experiment_type": 7,
    "gamma": 0.06,
    "induce_burn": False,
    "low_res_pass_strat": False,
    "max_crystal_vdim": 0.05,
    "max_crystal_vphi": 90,
    "min_crystal_vdim": 0.05,
    "min_crystal_vphi": 0.0,
    "min_dose": 30.0,
    "min_time": 0.0,
    "opt_sad": False,
    "permitted_phi_end": 360,
    "permitted_phi_start": 0.0,
    "rad_suscept": 1.0,
    "sad_res": 0.5,
    "space_group": "",
    "strategy_complexity": 0,
    "use_aimed_multiplicity": False,
    "use_aimed_resolution": False,
    "use_min_dose": True,
    "use_min_time": False,
    "use_permitted_rotation": False,
}

default_mesh_params = {
    "acq_parameters": {
        "cell_counting": "zig-zag",
        "cell_spacing": "vertical, horizontal",
        "detector_mode": 1,
        "exp_time": 10,
        "first_image": 1,
        "inverse_beam": False,
        "kappa": 11.0,
        "kappa_phi": 22.0,
        "num_images": 100,
        "num_passes": 1,
        "osc_range": 0.1,
        "overlap": 0,
        "prefixTemplate": "{PREFIX}_{POSITION}",
        "shutterless": True,
        "skip_existing_images": False,
        "subDirTemplate": "{ACRONYM}/{ACRONYM}-{NAME}",
        "take_dark_current": True,
        "take_snapshots": True,
    }
}

default_xrf_parameters = {"exp_time": "5"}
