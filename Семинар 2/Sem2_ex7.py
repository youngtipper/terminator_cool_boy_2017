'''''
Вежливый ежик идет по лесу, а навстречу ему три богатыря.
Ёжик: - Здравствуй, Илья Муромец!
Илья Муромец: - Здравствуй, ежик!
Ёжик: - Здравствуй, лошадь Ильи Муромца!
Лошадь: - Здравствуй, ежик!
Ёжик: - Здравствуй, добрыня Никитич!
Добрыня Никитич: - Здравствуй, ежик!
Ёжик: - Здравствуй, лошадь Добрыни Никитича!
Лошадь: - Здравствуй, ежик!
Ёжик: - Здравствуй, Алеша Попович!
Алеша Попович: - Здравствуй, ежик!
Ёжик: - Здравствуй, лошадь Алеши Поповича!
Лошадь: - Здравствуй, ежик!
... Проезжают...
Ёжик: - До свиданья, Илья Муромец!
Илья Муромец: - До свиданья, ежик!
Ёжик: - До свиданья, лошадь Ильи Муромца!
Лошадь: - До свиданья, ежик!
Ёжик: - До свиданья, добрыня Никитич!
Добрыня Никитич: - До свиданья, ежик!
Ёжик: - До свиданья, лошадь Добрыни Никитича!
Лошадь: - До свиданья, ежик!
Ёжик: - До свиданья, Алеша Попович!
Алеша Попович: - До свиданья, ежик!
Ёжик: - До свиданья, лошадь Алеши Поповича!
Лошадь: - До свиданья, ежик!
Идет ежик дальше, видит, навстречу ему Али-Баба и 40 разбойников.
Ёжик к ним: - Здравствуй, Али-Баба!
- Иди ты %№"?*, ежик, мы опаздываем!
'''

spisok777 = list(map(int, input().split()))
nazoyliviy_bratishka = 0
nomer_nadoedlivogo_chuvaka = 0
for i in spisok777:
    count = spisok777.count(i)
    if count > nazoyliviy_bratishka:
        nazoyliviy_bratishka = count
        nomer_nadoedlivogo_chuvaka = i
print(nomer_nadoedlivogo_chuvaka)