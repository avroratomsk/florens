// import "./import/modules";
// import "./import/components";
// import "./import/inputMask";
// import "./import/script";

// new VenoBox({
//   selector: ".index-gallery__item"
// });



/**
 * Всплывающее окно для чтения ответа на вопросы
 */

const faqBtn = document.querySelectorAll('.read-answer');

if (faqBtn) {
  faqBtn.forEach(btn => {
    btn.addEventListener('click', function (e) {
      let parent = this.closest('.faq__item');
      let title = parent.querySelector('.faq__item-title').innerText;
      let description = parent.querySelector('.faq__item-description').innerText;
      const popup_answer = document.getElementById('read-answer');
      popup_answer.classList.add('_open');
      bodyLock();
      popup_answer.querySelector('.popup__title').innerText = title;
      popup_answer.querySelector('.popup__description').innerText = description;
    })
  })
}

/**
 * Функция отктия и закрытия строку поиска  и фильтрацию по убыванию/возрастанию
 * 
 * Оптимизировать код
 */

const openSearchBtn = document.getElementById('open-search');
if (openSearchBtn) {
  openSearchBtn.addEventListener('click', function (e) {
    this.classList.toggle('_active');
    document.getElementById('single-search').classList.toggle('_active');

    if (!this.classList.contains('_active')) {
      this.innerHTML = '<i class="fa-solid fa-magnifying-glass"></i>';
    } else {
      this.innerHTML = '<i class="fa-solid fa-xmark"></i>';
    }
  })
}

const openFilterBtn = document.getElementById('open-filter');
if (openFilterBtn) {
  openFilterBtn.addEventListener('click', function (e) {
    this.classList.toggle('_active');
    document.getElementById('filter-sort').classList.toggle('_active');

    if (!this.classList.contains('_active')) {
      this.innerHTML = '<i class="fa-solid fa-sliders"></i>';
    } else {
      this.innerHTML = '<i class="fa-solid fa-xmark"></i>';
    }
  })
}

/**
 * Фильтр по цене 
 * 
 * Разобраться в скрипке 
 */

const rangeInput = document.querySelectorAll(".price-input__range input");
const priceInputField = document.querySelectorAll(".price-input__field input");
const progress = document.querySelector('#prodgress');
const priceGap = 1000;


if (rangeInput) {
  rangeInput.forEach(input => {
    input.addEventListener('input', (e) => {
      const minValue = parseInt(rangeInput[0].value);
      const maxValue = parseInt(rangeInput[1].value);

      if (maxValue - minValue < priceGap) {
        if (e.target.className === "price-input__range-min") {
          rangeInput[0].value = maxValue - priceGap;
        } else {
          rangeInput[1].value = minValue + priceGap;
        }
      } else {
        priceInputField[0].value = minValue;
        priceInputField[1].value = maxValue;
        progress.style.left = (minValue / rangeInput[0].max) * 100 + "%";
        progress.style.right = 100 - (maxValue / rangeInput[1].max) * 100 + "%";
      }


    })

  })
}


/**
 * Рейтинг в виде звездочек
 */

const ratingItemList = document.querySelectorAll('.form__star');
const inputSaveRating = document.querySelector('#form-reviews__rating');
if (ratingItemList) {
  const ratingItemArray = Array.prototype.slice.call(ratingItemList);

  ratingItemArray.forEach(item => {
    item.addEventListener('click', function (e) {
      const { rating } = item.dataset;
      item.parentNode.dataset.ratingTotal = rating;
      // inputSaveRating.value = rating;
    })
  })
}

/**
 * Просмотр полного описания продукта
 */

const btnViewProduct = document.querySelectorAll('.product-desc');
if (btnViewProduct) {
  btnViewProduct.forEach(btn => btn.addEventListener('click', viewProduct));
}

function viewProduct(e) {
  let parentNodeHtml = this.closest('.card-product').querySelector('.card-product__info').innerHTML;
  let popupView = document.querySelector('.popup-view .popup__grid');
  console.log(popupView);

  if (popupView) {
    popupView.innerHTML = parentNodeHtml;
  }
}

const orderBtn = document.querySelectorAll('.filter-sort__value');

orderBtn.forEach(btn => {
  btn.addEventListener('click', function (e) {
    // e.preventDefault();
  })
})


// Создание правильной ссылка номера телефона
const regNum = document.querySelectorAll('.reg-num');
if (regNum) {
  regNum.forEach(num => {
    phoneNumber = num.href.replace('tel:', '');
    newNumber = clearSimvol(phoneNumber.replace('8', "+7"));
    num.href = newNumber
  });
}
function clearSimvol(str) {
  return str.replace(/[\s.,%,),(,-]/g, '');
}

/**
 * Функции отвечающие за открытие и закрытие мини-корзины
 */

const showCart = document.getElementById('show-cart');
if (showCart) {
  showCart.addEventListener('click', showMiniCart);
}

function showMiniCart(e) {
  document.querySelector('#mini-cart').classList.add('_show-mini-cart');
  bodyLock();
}

const closeCart = document.getElementById('close-cart');
if (closeCart) {
  closeCart.addEventListener('click', closeMiniCart);
}

function closeMiniCart(e) {
  document.querySelector('#mini-cart').classList.remove('_show-mini-cart');
  bodyUnLock();
}

/**
 * Вспомогательные общие функции
 */

function bodyLock(e) {
  let widthScrollBar = window.innerWidth - document.documentElement.clientWidth;
  document.documentElement.style.marginRight = widthScrollBar + 'px';
  document.documentElement.classList.add('_lock');
}

function bodyUnLock(e) {
  document.documentElement.style.marginRight = '0px';
  document.documentElement.classList.remove('_lock');
}

/**
 * Работа с добавление в корзину без перезагрузки страницы
 */

let addToCartButton = document.querySelectorAll('.add-to-cart');

// if (addToCartButton) {
//   addToCartButton.forEach(btn => [
//     btn.addEventListener('click', addToCart)
//   ])
// }

// function addToCart(e) {
//   e.preventDefault();
//   // let miniCartCount = parseInt(document.querySelector('#mini-cart-count').textContent) || 0;
//   let productId = this.getAttribute('data-product-id');
//   console.log(productId);
//   let productLink = this.getAttribute('href');
//   console.log(productLink);
//   let csrfToken = document.querySelector('[name="csrfmiddlewaretoken"]').value;
//   console.log(csrfToken);

//   fetch('/cart/', {
//     method: 'POST',
//     headers: {
//       // "Accept": "application/json",
//       'Content-Type': 'application/json',
//       "X-CSRFToken": csrfToken
//     },
//     body: JSON.stringify(productId)
//   })
//     .then(response => response.json())
//     .then(data => { console.log(data) })
//     .catch(error => {
//       console.error('Ошибка при отправке данных:', error);
//     })

// fetch('/cart/cart_add/', {
//   method: 'POST',
//   headers: {
//     "Accept": "application/json",
//     'Content-Type': 'application/json',
//     'X-CSRFToken': csrfToken
//   },
//   body: JSON.stringify({ product_id: productId })
// })
//   .then(response => {
//     if (!response.ok) {
//       throw new Error('Network response was not ok');
//     }
//     const contentType = response.headers.get('content-type');
//     if (contentType && contentType.includes('application/json')) {
//       return response.json();
//     } else {
//       throw new Error('Unexpected response type');
//     }
//   })
//   .then(data => {
//     console.log(data);
//     // miniCartCount++;
//     let cartItemsContainer = document.querySelector('#cart-item');
//     cartItemsContainer.innerHTML = data.cart_items_html;
//     // document.querySelector('#mini-cart-count').textContent = miniCartCount; // Обновляем счетчик товаров в мини-корзине
//   })
//   .catch(error => {
//     console.error('Ошибка:', error);
//   });
// }

const whoGetRadio = document.querySelectorAll('.who-get');
if (whoGetRadio) {
  whoGetRadio.forEach(item => {
    item.addEventListener('change', function (e) {
      console.log(this);
      if (item.dataset.id == 'another') {
        document.getElementById('contact-human').classList.add('_show')
      } else {
        document.getElementById('contact-human').classList.remove('_show')
      }
    })
  })
}

const pickupCheckbox = document.getElementById('pickup');
if (pickupCheckbox) {
  pickupCheckbox.addEventListener('change', function (e) {
    if (!pickupCheckbox.checked) {
      document.getElementById('address-delivery').classList.add('_hidden');
    } else {
      document.getElementById('address-delivery').classList.remove('_hidden');
    }
  })
}



/**
 * Переключатели вкладок на странице продукта
 */

const tabProductTrigger = document.querySelectorAll('.specification-product__button');
const tabProductContent = document.querySelectorAll('.specification-product__info');

if (tabProductTrigger) {
  tabProductTrigger.forEach(btn => {
    btn.addEventListener('click', function (e) {
      let element = document.getElementById(this.dataset.id);
      tabProductContent.forEach(item => item.classList.remove('_show'));
      tabProductTrigger.forEach(item => item.classList.remove('_active'));
      this.classList.add('_active');
      element.classList.add('_show');
    })
  })
}

const burger = document.getElementById('burger');
if (burger) {
  burger.addEventListener('click', function (e) {
    console.log(this);
    document.querySelector('.header_mobile').classList.add('_show');
    bodyLock();
  })
}

const closeMenu = document.getElementById('close-menu');
if (closeMenu) {
  closeMenu.addEventListener('click', function (e) {
    console.log(this);
    document.querySelector('.header_mobile').classList.remove('_show');
    bodyUnLock();
  })
}

/**
 * Покупка в один клик
 */

const oneClickBtn = document.querySelectorAll('.card__click');
if (oneClickBtn) {
  oneClickBtn.forEach(btn => {
    btn.addEventListener('click', buyOneСlick)
  })
}

function buyOneСlick(e) {
  let parent = this.closest('.card');
  // let img = parent.querySelectorAll('.product-click-image')[0].src;

  let name = parent.querySelector('.card__title-h3').innerText;
  let price = parent.querySelector('.card__price').innerText;
  popup = document.getElementById('popup-one-click');

  // document.querySelector('.popup__product-img').src = img;
  document.querySelector('.popup__product-name').innerText = name;
  document.querySelector('.product__price-text').innerText = price;
  popup.classList.add('_open');
  bodyLock();

}

let popupBtn = document.querySelectorAll('[data-popup]')

if (popupBtn) {
  popupBtn.forEach(btn => {
    btn.addEventListener('click', openPopup);
  })
}

function openPopup(e) {
  document.getElementById(this.dataset.popup).classList.add('_open');
  bodyLock();
}

window.addEventListener('DOMContentLoaded', function (e) {
  const param_mass = []
  var params = window.location.search.replace('?', '').split('&');
  params.forEach(item => {
    param_mass.push(item.split('=')[0]);
  });
  if (param_mass[0] != '') {
    param_mass.forEach(item => {
      let checkbox = document.querySelector('[name=' + item + ']')
      checkbox.checked = true;
    })
  } else {
    console.log('Четко');
  }
})

const categoryDetailsFilterBtn = document.querySelector('.category-details__filter');
if (categoryDetailsFilterBtn) {
  categoryDetailsFilterBtn.addEventListener('click', function (e) {
    document.getElementById('filter-category').classList.add('_show');
    bodyLock();
  })
}

const closeFilter = document.getElementById('close-filter');
if (closeFilter) {
  closeFilter.addEventListener('click', function (e) {
    document.getElementById('filter-category').classList.remove('_show');
    bodyUnLock();
  })
}


const closeBtn = document.querySelectorAll('.close-btn');
if (closeBtn) {
  closeBtn.forEach(btn => {
    btn.addEventListener('click', function (e) {
      let parent = this.closest('.popup');
      parent.classList.remove('_open');
      bodyUnLock();
    })
  })
}

// document.getElementById('apply-filter').addEventListener('click', function (e) {
//   e.target.preventDefault();
//   var checkedValues = Array.from(document.querySelectorAll('input[name="diametr"]:checked')).map(function (el) {
//     return el.value;
//   });
//   var params = new URLSearchParams(window.location.search);
//   console.log(params);
//   params.set('diametr', checkedValues.join(','));
//   window.location.search = params.toString();
// });



// Ловим собыитие клика по кнопке добавить в корзину
$(document).on("click", ".add-to-cart", function (e) {
  // Блокируем его базовое действие
  e.preventDefault();

  // Берем элемент счетчика в значке корзины и берем оттуда значение
  var goodsInCartCount = $("#mini-cart-count");
  var cartCount = parseInt(goodsInCartCount.text() || 0);

  // Получаем id товара из атрибута data-product-id
  var product_id = $(this).data("product-id");

  // Из атрибута href берем ссылку на контроллер django
  var add_to_cart_url = $(this).attr("href");
  console.log(add_to_cart_url);

  // делаем post запрос через ajax не перезагружая страницу
  $.ajax({
    type: "POST",
    url: add_to_cart_url,
    data: {
      product_id: product_id,
      csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
    },
    success: function (data) {
      $("#notification-modal .success__body").html('<div class="success__body-inner"><p class="success__name">' + data.product_name + '</p> <p  class="success__price">' + data.product_price + '₽</p></div> <div class="success__image"><img src="' + data.product_image + '" alt=""></div>');
      $("#notification-modal").addClass("show");

      // Закрытие модального окна после 5 секунд
      setTimeout(function () {
        $("#notification-modal").removeClass("show");
      }, 5000);

      $('#show-cart').append('<div class="no-empty"></div>');



      // Увеличиваем количество товаров в корзине (отрисовка в шаблоне)
      cartCount++;
      goodsInCartCount.text(cartCount);
      if (cartCount > 0) {
        $('#mini-cart__inner').html('<h4 class="mini-cart__title">Корзина<span>(</span><strong id="mini-cart-count">' + cartCount + ' </strong><span>)<span></h4><div class="mini-cart__inner" id="cart-item">{% include "components/cart-item.html" %}</div>')

        $('#mini-cart').append('<div class="mini-cart__links"><a href="/orders/create/" class="mini-cart__link">Оформить заказ</a></div>')
      }
      // Меняем содержимое корзины на ответ от django (новый отрисованный фрагмент разметки корзины)
      var cartItemsContainer = $("#cart-item");
      cartItemsContainer.html(data.cart_items_html);
    },

    error: function (data) {
      console.log("Ошибка при добавлении товара в корзину");
    },
  });
});

$(document).on("click", ".remove-from-cart", function (e) {
  // Блокируем его базовое действие
  e.preventDefault();

  // Берем элемент счетчика в значке корзины и берем оттуда значение
  var goodsInCartCount = $("#mini-cart-count");
  var cartCount = parseInt(goodsInCartCount.text() || 0);

  // Получаем id корзины из атрибута data-cart-id
  var cart_id = $(this).data("cart-id");
  // Из атрибута href берем ссылку на контроллер django
  var remove_from_cart = $(this).attr("href");
  console.log(remove_from_cart);
  console.log($("[name=csrfmiddlewaretoken]").val());
  // делаем post запрос через ajax не перезагружая страницу
  $.ajax({
    type: "POST",
    url: remove_from_cart,
    data: {
      cart_id: cart_id,
      csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
    },
    success: function (data) {
      // Уменьшаем количество товаров в корзине (отрисовка)
      cartCount -= data.quantity_deleted;
      goodsInCartCount.text(cartCount);

      if (cartCount == 0) {
        $('#show-cart .no-empty').remove();
        $('#mini-cart__inner').html('<div class="mini-cart__empty" id="mini-cart__empty"><p class="mini-cart__empty-text">Корзина пуста</p><a href="{% url "category" %}"class="mini-cart__empty-link">Перейти в каталог</a></div>')
        $('#mini-cart .mini-cart__links').remove()
      }
      console.log(cartCount);
      // Меняем содержимое корзины на ответ от django (новый отрисованный фрагмент разметки корзины)
      var cartItemsContainer = $("#cart-item");
      cartItemsContainer.html(data.cart_items_html);
    },

    error: function (data) {
      console.log("Ошибка при добавлении товара в корзину");
    },
  });
});


