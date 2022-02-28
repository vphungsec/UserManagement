class TrainingViewModel {
    constructor() {
        this.fetchTrainingsByUser();
    }

    fetchTrainingsByUser = function () {
        return fetch('get_by_employee', {credentials: 'same-origin'}).then(jsonOrThrow);
    };
}