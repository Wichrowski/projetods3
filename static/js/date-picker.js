function datePicker(selector) {

  var field = document.querySelector(selector);

  var picker = new Pikaday({
    field: document.querySelector(selector),
    format: 'DD/MM/YYYY',
    i18n: {
      previousMonth: 'Mês anterior',
      nextMonth: 'Próximo mês',
      months: ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro'],
      weekdays: ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'],
      weekdaysShort: ['Dom','Seg','Ter','Qua','Qui','Sex','Sab']
    },
    toString: function(date, format) {
      var day = date.getDate();
      var month = date.getMonth() + 1;
      var year = date.getFullYear();

      day = day < 10
        ? '0' + day
        : day;

      month = month < 10
        ? '0' + month
        : month;

      return `${day}/${month}/${year}`;
    }
  });

  return picker;
}
