function MessageViewModel() {
    let self = this;
    self.messages = ko.observableArray([]);
}

MessageViewModel.prototype.clearMessage = function () {
    let self = this;
    self.messages([]);
}

MessageViewModel.prototype.pushMessage = function (mess) {
    let self = this;
    self.messages.push(mess);
}