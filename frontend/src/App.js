import React, { useEffect, useState } from 'react';
import './App.css';

const API_URL = process.env.REACT_APP_API_URL;

// Jednoduchý komponent pre modálne potvrdenie
function ModalConfirm({ message, onConfirm, onCancel }) {
  return (
    <div className="modal-overlay">
      <div className="modal-content">
        <p>{message}</p>
        <div className="modal-buttons">
          <button className="btn-confirm" onClick={onConfirm}>Áno</button>
          <button className="btn-cancel" onClick={onCancel}>Zrušiť</button>
        </div>
      </div>
    </div>
  );
}

function App() {
  const [token, setToken] = useState(localStorage.getItem("token") || "");
  const [pouzivatel, setPouzivatel] = useState(localStorage.getItem("meno") || "");
  const [meno, setMeno] = useState("");
  const [heslo, setHeslo] = useState("");
  const [jeRegistracia, setJeRegistracia] = useState(false);
  const [chybovaHlasla, setChybovaHlasla] = useState("");
  const [uspesnaHlasla, setUspesnaHlasla] = useState("");
  const [ulohy, setUlohy] = useState([]);
  const [nazov, setNazov] = useState("");
  const [popis, setPopis] = useState("");

  // Nové stavy pre modálne okno
  const [showModal, setShowModal] = useState(false);
  const [ulohaNaVymazanie, setUlohaNaVymazanie] = useState(null);

  useEffect(() => {
    if (token) nacitajUlohy();
  }, [token]);

  const nacitajUlohy = async () => {
    try {
      const odpoved = await fetch(`${API_URL}/tasks`, {
        headers: { Authorization: `Bearer ${token}` },
      });

      if (!odpoved.ok) {
        throw new Error("Neautorizovaný prístup – token je neplatný alebo expiroval.");
      }

      const data = await odpoved.json();
      if (!Array.isArray(data)) {
        throw new Error("Očakávali sme pole úloh, ale dostali sme niečo iné.");
      }

      setUlohy(data);
    } catch (err) {
      console.error("Chyba pri načítaní úloh:", err);
      setChybovaHlasla("Prihlásenie expirovalo alebo nastala chyba. Prihlás sa znova.");
      setUspesnaHlasla("");
      odhlas();
    }
  };

  const pridajUlohu = async () => {
    if (!nazov || !popis) {
      setChybovaHlasla("Zadaj názov aj popis.");
      setUspesnaHlasla("");
      return;
    }

    try {
      const odpoved = await fetch(`${API_URL}/tasks`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({ nazov, popis }),
      });
      if (!odpoved.ok) throw new Error("Chyba pri vytváraní úlohy");
      setNazov("");
      setPopis("");
      setChybovaHlasla("");
      setUspesnaHlasla("");
      nacitajUlohy();
    } catch (err) {
      console.error(err);
      setChybovaHlasla("Nepodarilo sa pridať úlohu.");
      setUspesnaHlasla("");
    }
  };

  const zmenStav = async (id, novyStav) => {
    try {
      await fetch(`${API_URL}/tasks/${id}`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({ stav: novyStav }),
      });
      nacitajUlohy();
    } catch (err) {
      console.error("Chyba pri zmene stavu:", err);
    }
  };

  // Teraz iba otvor modálne okno pri kliknutí
  const otvorModalNaVymazanie = (uloha) => {
    setUlohaNaVymazanie(uloha);
    setShowModal(true);
  };

  // Po potvrdení odstráni úlohu a zavrie modál
  const potvrditVymazanie = async () => {
    if (!ulohaNaVymazanie) return;
    try {
      await fetch(`${API_URL}/tasks/${ulohaNaVymazanie.id}`, {
        method: "DELETE",
        headers: { Authorization: `Bearer ${token}` },
      });
      nacitajUlohy();
      setShowModal(false);
      setUlohaNaVymazanie(null);
    } catch (err) {
      console.error("Chyba pri odstraňovaní úlohy:", err);
      setShowModal(false);
      setUlohaNaVymazanie(null);
    }
  };

  // Zavrie modálne okno bez vymazania
  const zrusitVymazanie = () => {
    setShowModal(false);
    setUlohaNaVymazanie(null);
  };

  const prihlasPouzivatela = async () => {
    setChybovaHlasla("");
    setUspesnaHlasla("");
    if (!meno || !heslo) {
      setChybovaHlasla("Zadaj meno aj heslo.");
      return;
    }

    try {
      const odpoved = await fetch(`${API_URL}/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ meno, heslo }),
      });
      const data = await odpoved.json();
      if (data.token) {
        localStorage.setItem("token", data.token);
        localStorage.setItem("meno", meno);
        setToken(data.token);
        setPouzivatel(meno);
        setChybovaHlasla("");
        setUspesnaHlasla("");
      } else {
        setChybovaHlasla(data.error || "Prihlásenie zlyhalo.");
        setUspesnaHlasla("");
      }
    } catch (err) {
      console.error("Chyba pri prihlasovaní:", err);
      setChybovaHlasla("Chyba na strane servera.");
      setUspesnaHlasla("");
    }
  };

  const registrujPouzivatela = async () => {
    setChybovaHlasla("");
    setUspesnaHlasla("");

    if (!meno || !heslo) {
      setChybovaHlasla("Zadaj meno aj heslo.");
      return;
    }

    if (heslo.length < 6 || !/[a-zA-Z]/.test(heslo) || !/\d/.test(heslo)) {
      setChybovaHlasla("Heslo musí mať aspoň 6 znakov a obsahovať písmená aj čísla.");
      return;
    }

    try {
      const odpoved = await fetch(`${API_URL}/register`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ meno, heslo }),
      });
      const data = await odpoved.json();
      if (odpoved.status === 201) {
        setJeRegistracia(false);
        setUspesnaHlasla("Registrácia bola úspešná. Teraz sa prihlás.");
        setMeno("");
        setHeslo("");
      } else {
        setChybovaHlasla(data.error || "Registrácia zlyhala.");
        setUspesnaHlasla("");
      }
    } catch (err) {
      console.error("Chyba pri registrácii:", err);
      setChybovaHlasla("Chyba na strane servera.");
      setUspesnaHlasla("");
    }
  };

  const odhlas = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("meno");
    setToken("");
    setPouzivatel("");
    setMeno("");
    setHeslo("");
    setUlohy([]);
    setChybovaHlasla("");
    setUspesnaHlasla("");
  };

  const renderUlohy = (stav) =>
    ulohy
      .filter((u) => u.stav === stav)
      .map((u) => (
        <li key={u.id}>
          <strong>{u.nazov}</strong>: {u.popis} | Stav: {u.stav}
          {stav === "Nezahájená" && (
            <>
              <button onClick={() => zmenStav(u.id, "Prebieha")}>Prebieha</button>
              <button onClick={() => otvorModalNaVymazanie(u)}>Odstrániť</button>
            </>
          )}
          {stav === "Prebieha" && (
            <>
              <button onClick={() => zmenStav(u.id, "Hotová")}>Hotová</button>
              <button onClick={() => otvorModalNaVymazanie(u)}>Odstrániť</button>
            </>
          )}
          {stav === "Hotová" && <button onClick={() => otvorModalNaVymazanie(u)}>Odstrániť</button>}
        </li>
      ));

  if (!token) {
    return (
      <div className="fade-in" style={{ padding: "20px", maxWidth: "400px", margin: "auto" }}>
        <h2>{jeRegistracia ? "Registrácia" : "Prihlásenie"}</h2>

        {chybovaHlasla && (
          <div className="error">{chybovaHlasla}</div>
        )}

        {uspesnaHlasla && (
          <div className="success">{uspesnaHlasla}</div>
        )}

        <div>
          <label htmlFor="meno">Používateľské meno</label>
          <input
            id="meno"
            type="text"
            placeholder="Zadaj meno"
            value={meno}
            onChange={(e) => setMeno(e.target.value)}
          />
        </div>

        <div>
          <label htmlFor="heslo">Heslo</label>
          <input
            id="heslo"
            type="password"
            placeholder="Zadaj heslo"
            value={heslo}
            onChange={(e) => setHeslo(e.target.value)}
          />
        </div>

        {jeRegistracia ? (
          <>
            <button onClick={registrujPouzivatela}>Registrovať</button>
            <p>
              Už máš účet?{" "}
              <button onClick={() => { setJeRegistracia(false); setChybovaHlasla(""); setUspesnaHlasla(""); }}>
                Prihlásiť sa
              </button>
            </p>
          </>
        ) : (
          <>
            <button onClick={prihlasPouzivatela}>Prihlásiť</button>
            <p>
              Nemáš účet?{" "}
              <button onClick={() => { setJeRegistracia(true); setChybovaHlasla(""); setUspesnaHlasla(""); }}>
                Registrovať sa
              </button>
            </p>
          </>
        )}
      </div>
    );
  }

  return (
    <div style={{ padding: "20px" }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", flexWrap: "wrap" }}>
        <h1>Task Manager 2.0 – React Frontend</h1>
        <div>
          <span style={{ marginRight: "10px" }}>👤 {pouzivatel}</span>
          <button onClick={odhlas}>Odhlásiť</button>
        </div>
      </div>

      {chybovaHlasla && (
        <div className="error">{chybovaHlasla}</div>
      )}

      {uspesnaHlasla && (
        <div className="success">{uspesnaHlasla}</div>
      )}

      <input type="text" placeholder="Zadaj názov" value={nazov} onChange={(e) => setNazov(e.target.value)} />
      <input type="text" placeholder="Zadaj popis" value={popis} onChange={(e) => setPopis(e.target.value)} />
      <button onClick={pridajUlohu}>Pridať</button>

      <h2>🕒 Nezahájené úlohy</h2>
      <ul>{renderUlohy("Nezahájená")}</ul>

      <h2>🌺 Prebiehajúce úlohy</h2>
      <ul>{renderUlohy("Prebieha")}</ul>

      <h2>✅ Hotová úlohy</h2>
      <ul>{renderUlohy("Hotová")}</ul>

      {showModal && (
        <ModalConfirm
          message="Naozaj chceš úlohu vymazať?"
          onConfirm={potvrditVymazanie}
          onCancel={zrusitVymazanie}
        />
      )}
    </div>
  );
}

export default App;
