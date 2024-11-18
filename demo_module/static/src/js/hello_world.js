function onChangeDateAllowed (ev) {
    let div = this.$('select[name="date_allowed"]').parent();

    if (ev.target.value === 'ja') {
        div.attr("hidden", false);
    } else {
        div.attr("hidden", true);
    }
}