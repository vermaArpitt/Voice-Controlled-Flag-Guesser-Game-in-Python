import pygame as p
import game_level
import game_over
import end_screen

Flags = {}

def loadFlags(dic):
    for key in dic.keys():
        Flags[key] = p.image.load("flags/" + key + ".png")

def game_loop(screen):
    dic = {'af' : 'Afghanistan',
           'al' : 'Albania',
           'dz' : 'Algeria',
           'ad' : 'Andorra',
           'ao' : 'Angola',
           'ag' : 'Antigua and Barbuda',
           'ar' : 'Argentina',
           'am' : 'Armenia',
           'au' : 'Australia',
           'at' : 'Austria',
           'az' : 'Azerbaijan',
           'bs' : 'Bahamas',
           'bh' : 'Bahrain',
           'bd' : 'Bangladesh',
           'bb' : 'Barbados',
           'by' : 'Belarus',
           'be' : 'Belgium',
           'bz' : 'Belize',
           'bj' : 'Benin',
           'bt' : 'Bhutan',
           'bo' : 'Bolivia',
           'ba' : 'Bosnia and Herzegovina',
           'bw' : 'Botswana',
           'br' : 'Brazil',
           'bn' : 'Brunei',
           'bg' : 'Bulgaria',
           'bf' : 'Burkina Faso',
           'bi' : 'Burundi',
           'kh' : 'Cambodia',
           'cm' : 'Cameroon',
           'ca' : 'Canada',
           'cv' : 'Cape Verde',
           'cf' : 'Central African Republic',
           'td' : 'Chad',
           'cl' : 'Chile',
           'cn' : 'China',
           'co' : 'Colombia',
           'km' : 'Comoros',
           'cg' : 'Republic of the Congo',
           'cd' : 'Democratic Republic of Congo',
           'cr' : 'Costa Rica',
           'ci' : "Côte d'Ivoire",
           'hr' : 'Croatia',
           'cu' : 'Cuba',
           'cy' : 'Cyprus',
           'cz' : 'Czechia',
           'dk' : 'Denmark',
           'dj' : 'Djibouti',
           'dm' : 'Dominica',
           'do' : 'Dominican Republic',
           'ec' : 'Ecuador',
           'eg' : 'Egypt',
           'sv' : 'El Salvador',
           'gq' : 'Equatorial Guinea',
           'er' : 'Eritrea',
           'ee' : 'Estonia',
           'sz' : 'Eswatini',
           'et' : 'Ethiopia',
           'fj' : 'Fiji',
           'fi' : 'Finland',
           'fr' : 'France',
           'ga' : 'Gabon',
           'gm' : 'Gambia',
           'ge' : 'Georgia',
           'de' : 'Germany',
           'gh' : 'Ghana',
           'gr' : 'Greece',
           'gd' : 'Grenada',
           'gt' : 'Guatemala',
           'gn' : 'Guinea',
           'gw' : 'Guinea-Bissau',
           'gy' : 'Guyana',
           'ht' : 'Haiti',
           'hn' : 'Honduras',
           'hu' : 'Hungary',
           'is' : 'Iceland',
           'in' : 'India',
           'id' : 'Indonesia',
           'ir' : 'Iran',
           'iq' : 'Iraq',
           'ie' : 'Ireland',
           'il' : 'Israel',
           'it' : 'Italy',
           'jm' : 'Jamaica',
           'jp' : 'Japan',
           'jo' : 'Jordan',
           'kz' : 'Kazakhstan',
           'ke' : 'Kenya',
           'ki' : 'Kiribati',
           'kp' : 'North Korea',
           'kr' : 'South Korea',
           'kw' : 'Kuwait',
           'kg' : 'Kyrgyzstan',
           'la' : 'Laos',
           'lv' : 'Latvia',
           'lb' : 'Lebanon',
           'ls' : 'Lesotho',
           'lr' : 'Liberia',
           'ly' : 'Libya',
           'li' : 'Liechtenstein',
           'lt' : 'Lithuania',
           'lu' : 'Luxembourg',
           'mg' : 'Madagascar',
           'mw' : 'Malawi',
           'my' : 'Malaysia',
           'mv' : 'Maldives',
           'ml' : 'Mali',
           'mt' : 'Malta',
           'mh' : 'Marshall Islands',
           'mr' : 'Mauritania',
           'mu' : 'Mauritius',
           'mx' : 'Mexico',
           'fm' : 'Micronesia',
           'md' : 'Moldova',
           'mc' : 'Monaco',
           'mn' : 'Mongolia',
           'me' : 'Montenegro',
           'ma' : 'Morocco',
           'mz' : 'Mozambique',
           'mm' : 'Myanmar',
           'na' : 'Namibia',
           'nr' : 'Nauru',
           'np' : 'Nepal',
           'nl' : 'Netherlands',
           'nz' : 'New Zealand',
           'ni' : 'Nicaragua',
           'ne' : 'Niger',
           'ng' : 'Nigeria',
           'mk' : 'North Macedonia',
           'no' : 'Norway',
           'om' : 'Oman',
           'pk' : 'Pakistan',
           'pw' : 'Palau',
           'ps' : 'Palestine',
           'pa' : 'Panama',
           'pg' : 'Papua New Guinea',
           'py' : 'Paraguay',
           'pe' : 'Peru',
           'ph' : 'Philippines',
           'pl' : 'Poland',
           'pt' : 'Portugal',
           'qa' : 'Qatar',
           'ro' : 'Romania',
           'ru' : 'Russia',
           'rw' : 'Rwanda',
           'kn' : 'Saint Kitts and Nevis',
           'lc' : 'Saint Lucia',
           'vc' : 'Saint Vincent and the Grenadines',
           'ws' : 'Samoa',
           'sm' : 'San Marino',
           'st' : 'São Tomé and Príncipe',
           'sa' : 'Saudi Arabia',
           'sn' : 'Senegal',
           'rs' : 'Serbia',
           'sc' : 'Seychelles',
           'sl' : 'Sierra Leone',
           'sg' : 'Singapore',
           'sk' : 'Slovakia',
           'si' : 'Slovenia',
           'sb' : 'Solomon Islands',
           'so' : 'Somalia',
           'za' : 'South Africa',
           'ss' : 'South Sudan',
           'es' : 'Spain',
           'lk' : 'Sri Lanka',
           'sd' : 'Sudan',
           'sr' : 'Suriname',
           'se' : 'Sweden',
           'ch' : 'Switzerland',
           'sy' : 'Syria',
           'tj' : 'Tajikistan',
           'tz' : 'Tanzania',
           'th' : 'Thailand',
           'tl' : 'Timor-Leste',
           'tg' : 'Togo',
           'to' : 'Tonga',
           'tt' : 'Trinidad and Tobago',
           'tn' : 'Tunisia',
           'tr' : 'Turkey',
           'tm' : 'Turkmenistan',
           'tv' : 'Tuvalu',
           'ug' : 'Uganda',
           'ua' : 'Ukraine',
           'ae' : 'United Arab Emirates',
           'gb' : 'United Kingdom',
           'us' : 'United States',
           'uy' : 'Uruguay',
           'uz' : 'Uzbekistan',
           'vu' : 'Vanuatu',
           'va' : 'Vatican City',
           've' : 'Venezuela',
           'vn' : 'Vietnam',
           'ye' : 'Yemen',
           'zm' : 'Zambia',
           'zw' : 'Zimbabwe'}
    loadFlags(dic)

    #Initializing Score and Lives
    score = 0
    lives = 3

    for key, value in dic.items():
        score, lives = game_level.game_level(screen, score, lives, Flags[key], value)
        # score = new_score
        if lives == 0:
            game_over.game_over(screen, score)
            p.quit()
        elif score == -2:
            p.quit()

    end_screen.end_screen(screen, score)