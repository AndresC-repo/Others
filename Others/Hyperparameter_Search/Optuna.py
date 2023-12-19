import sys

import optuna
from optuna.trial import TrialState

from ____ import create_folder
from ____ import objective_function

"""
    Optuna HP search. To be called from main_Prediction.py
"""


def optuna_optim_objective(config):
    
    # Wrap the objective inside a lambda and call objective inside it
    def objective(trial): return objective_function(trial, config)
    # Pass func to Optuna studies
    study = optuna.create_study(
        direction="minimize",
        study_name="Prediction_data_points",
        pruner=optuna.pruners.MedianPruner(n_warmup_steps=config['Optuna']["n_warmup_steps"]),
    )
    study.optimize(objective, n_trials=config['Optuna']["n_trials"])

    pruned_trials = study.get_trials(
        deepcopy=False, states=[TrialState.PRUNED])
    complete_trials = study.get_trials(
        deepcopy=False, states=[TrialState.COMPLETE])

    # Save the current standard output
    original_stdout = sys.stdout

    # Specify the file path where you want to save the output
    root_path = f'Prediction/saved_models/best_models_paramenteres/'
    model_title = f'{config["target"]}_best_model.txt'
    output_file_path = root_path + model_title
    create_folder(root_path)

    # Open the file in write mode
    with open(output_file_path, "w") as f:
        # Redirect standard output to the file
        sys.stdout = f
        print(f'  Target:  {config["target"]}')
        print(f'  Features:  {config["features"]}')
        print("Study statistics: ")
        print("  Number of finished trials: ", len(study.trials))
        print("  Number of pruned trials: ", len(pruned_trials))
        print("  Number of complete trials: ", len(complete_trials))
        print("Best trial:")
        trial = study.best_trial
        print("  Value: ", trial.value)
        print("  Params: ")
        for key, value in trial.params.items():
            print("    {}: {}".format(key, value))

    # Restore the original standard output
    sys.stdout = original_stdout

    print(f"Study statistics have been saved to: {output_file_path}")