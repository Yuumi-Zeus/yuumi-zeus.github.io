# `OdinEditorWindow class`
## Introduction
- NameSpace: `Sirenix.OdinInspector.Editor`
- Assembly: `Sirenix.OdinInspector.Editor`

``` csharp
[ShowOdinSerializedPropertiesInInspector]
public class OdinEditorWindow : UnityEditor.EditorWindow, UnityEngine.ISerializationCallbackReceiver
```

## Constructors
| 构造函数 | 注释 | Comment |
| :--- | :--- | :--- |
| `public OdinEditorWindow()` | 无 | No Comment |
## Methods
| 方法 | 注释 | Comment |
| :--- | :--- | :--- |
| `public static OdinEditorWindow CreateOdinEditorWindowInstanceForObject(Object obj)` | 无 | No Comment |
| `public static OdinEditorWindow InspectObject(Object obj)` | 无 | No Comment |
| `public static OdinEditorWindow InspectObject(OdinEditorWindow window, Object obj)` | 无 | No Comment |
| `public static OdinEditorWindow InspectObjectInDropDown(Object obj, Rect btnRect, float windowWidth)` | 无 | No Comment |
| `public static OdinEditorWindow InspectObjectInDropDown(Object obj, Rect btnRect, Vector2 windowSize)` | 无 | No Comment |
| `public static OdinEditorWindow InspectObjectInDropDown(Object obj, Vector2 position)` | 无 | No Comment |
| `public static OdinEditorWindow InspectObjectInDropDown(Object obj, float windowWidth)` | 无 | No Comment |
| `public static OdinEditorWindow InspectObjectInDropDown(Object obj, Vector2 position, float windowWidth)` | 无 | No Comment |
| `public static OdinEditorWindow InspectObjectInDropDown(Object obj, float width, float height)` | 无 | No Comment |
| `public static OdinEditorWindow InspectObjectInDropDown(Object obj)` | 无 | No Comment |
| `public void ShowToast(ToastPosition toastPosition, SdfIconType icon, string text, Color color, float duration)` | 无 | No Comment |
| `protected virtual void DrawEditor(int index)` | 无 | No Comment |
| `protected virtual void DrawEditorPreview(int index, float height)` | 无 | No Comment |
| `protected virtual void DrawEditors()` | 无 | No Comment |
| `protected void EnableAutomaticHeightAdjustment(int maxHeight, bool retainInitialWindowPosition)` | 无 | No Comment |
| `protected void EnsureEditorsAreReady()` | 无 | No Comment |
| `protected virtual Object GetTarget()` | 无 | No Comment |
| `protected virtual IEnumerable<Object> GetTargets()` | 无 | No Comment |
| `protected virtual void Initialize()` | 无 | No Comment |
| `protected virtual void OnAfterDeserialize()` | 无 | No Comment |
| `protected virtual void OnBeforeSerialize()` | 无 | No Comment |
| `protected virtual void OnBeginDrawEditors()` | 无 | No Comment |
| `protected virtual void OnDestroy()` | 无 | No Comment |
| `protected virtual void OnDisable()` | 无 | No Comment |
| `protected virtual void OnEnable()` | 无 | No Comment |
| `protected virtual void OnEndDrawEditors()` | 无 | No Comment |
| `protected virtual void OnImGUI()` | 无 | No Comment |
| `protected void UpdateEditors()` | 无 | No Comment |
| `internal static OdinEditorWindow CreateOdinEditorWindowInstanceForObject(Object obj, bool forceSerializeInspectedObject)` | 无 | No Comment |
| `internal static OdinEditorWindow InspectObject(Object obj, bool forceSerializeInspectedObject)` | 无 | No Comment |
| `private void Cleanup()` | 无 | No Comment |
| `private void CreateGUI()` | 无 | No Comment |
| `private void InitializeIfNeeded()` | 无 | No Comment |
| `private void SelectionChanged()` | 无 | No Comment |
| `private virtual void UnityEngine.ISerializationCallbackReceiver.OnAfterDeserialize()` | 无 | No Comment |
| `private virtual void UnityEngine.ISerializationCallbackReceiver.OnBeforeSerialize()` | 无 | No Comment |
| `[Obsolete] protected virtual void OnGUI()` | 无 | No Comment |

## Events
| 事件 | 注释 | Comment |
| :--- | :--- | :--- |
| `public event Action OnBeginGUI` | 无 | No Comment |
| `public event Action OnClose` | 无 | No Comment |
| `public event Action OnEndGUI` | 无 | No Comment |

## Properties
| 属性 | 注释 | Comment |
| :--- | :--- | :--- |
| `public OdinEditorWindow DefaultEditorPreviewHeight { public get; public set; }` | 无 | No Comment |
| `public OdinEditorWindow DefaultLabelWidth { public get; public set; }` | 无 | No Comment |
| `public OdinEditorWindow DrawUnityEditorPreview { public get; public set; }` | 无 | No Comment |
| `public OdinEditorWindow UseScrollView { public get; public set; }` | 无 | No Comment |
| `public OdinEditorWindow WindowPadding { public get; public set; }` | 无 | No Comment |
| `protected OdinEditorWindow CurrentDrawingTargets { protected get; }` | 无 | No Comment |
| `[Obsolete] public OdinEditorWindow PropertyTree { public get; }` | 无 | No Comment |

## Fields
| 字段 | 注释 | Comment |
| :--- | :--- | :--- |
| `public const int MAX_DROPDOWN_HEIGHT` | 无 | No Comment |
| `public const int MIN_DROPDOWN_HEIGHT` | 无 | No Comment |
| `private readonly Object[] EmptyObjectArray` | 无 | No Comment |
| `private static bool hasUpdatedOdinEditors` | 无 | No Comment |
| `private static int inspectObjectWindowCount` | 无 | No Comment |
| `private static PropertyInfo materialForceVisibleProperty` | 无 | No Comment |
| `private Action _onBeginGUI` | 无 | No Comment |
| `private Action _onEndGUI` | 无 | No Comment |
| `private Vector2 contenSize` | 无 | No Comment |
| `private Object[] currentTargets` | 无 | No Comment |
| `private ImmutableList<Object> currentTargetsImm` | 无 | No Comment |
| `private float defaultEditorPreviewHeight` | 无 | No Comment |
| `private bool drawUnityEditorPreview` | 无 | No Comment |
| `private Editor[] editors` | 无 | No Comment |
| `private Object inspectTargetObject` | 无 | No Comment |
| `private Object inspectorTargetSerialized` | 无 | No Comment |
| `private bool isAutoHeightAdjustmentReady` | 无 | No Comment |
| `private bool isInOurImGUIContainer` | 无 | No Comment |
| `private bool isInitialized` | 无 | No Comment |
| `private bool isInsideOnGUI` | 无 | No Comment |
| `private float labelWidth` | 无 | No Comment |
| `private GUIStyle marginStyle` | 无 | No Comment |
| `private int mouseDownId` | 无 | No Comment |
| `private int mouseDownKeyboardControl` | 无 | No Comment |
| `private EditorWindow mouseDownWindow` | 无 | No Comment |
| `private bool preventContentFromExpanding` | 无 | No Comment |
| `private PropertyTree[] propertyTrees` | 无 | No Comment |
| `private Vector2 scrollPos` | 无 | No Comment |
| `private SerializationData serializationData` | 无 | No Comment |
| `private List<Toast> toasts` | 无 | No Comment |
| `private bool useScrollView` | 无 | No Comment |
| `private int warmupRepaintCount` | 无 | No Comment |
| `private Vector4 windowPadding` | 无 | No Comment |
| `private int wrappedAreaMaxHeight` | 无 | No Comment |

## Inherited Members
| 成员 | 注释 | 声明此方法的类 |
| :--- | :--- | :--- |
| `public void BeginWindows()` | 无 | `UnityEditor.EditorWindow` |
| `public void Close()` | 无 | `UnityEditor.EditorWindow` |
| `public virtual void DiscardChanges()` | 无 | `UnityEditor.EditorWindow` |
| `public void EndWindows()` | 无 | `UnityEditor.EditorWindow` |
| `public virtual bool Equals(Object other)` | 无 | `UnityEngine.Object` |
| `public void Focus()` | 无 | `UnityEditor.EditorWindow` |
| `public virtual IEnumerable<Type> GetExtraPaneTypes()` | 无 | `UnityEditor.EditorWindow` |
| `public virtual int GetHashCode()` | 无 | `UnityEngine.Object` |
| `public int GetInstanceID()` | 无 | `UnityEngine.Object` |
| `public Type GetType()` | 无 | `System.Object` |
| `public void RemoveNotification()` | 无 | `UnityEditor.EditorWindow` |
| `public virtual void Repaint()` | 无 | `UnityEditor.EditorWindow` |
| `public virtual void SaveChanges()` | 无 | `UnityEditor.EditorWindow` |
| `public bool SendEvent(Event e)` | 无 | `UnityEditor.EditorWindow` |
| `public void Show()` | 无 | `UnityEditor.EditorWindow` |
| `public void Show(bool immediateDisplay)` | 无 | `UnityEditor.EditorWindow` |
| `public void ShowAsDropDown(Rect buttonRect, Vector2 windowSize)` | 无 | `UnityEditor.EditorWindow` |
| `public void ShowAuxWindow()` | 无 | `UnityEditor.EditorWindow` |
| `public void ShowModal()` | 无 | `UnityEditor.EditorWindow` |
| `public void ShowModalUtility()` | 无 | `UnityEditor.EditorWindow` |
| `public void ShowNotification(GUIContent notification, double fadeoutWait)` | 无 | `UnityEditor.EditorWindow` |
| `public void ShowNotification(GUIContent notification)` | 无 | `UnityEditor.EditorWindow` |
| `public void ShowPopup()` | 无 | `UnityEditor.EditorWindow` |
| `public void ShowTab()` | 无 | `UnityEditor.EditorWindow` |
| `public void ShowUtility()` | 无 | `UnityEditor.EditorWindow` |
| `public virtual string ToString()` | 无 | `UnityEngine.Object` |
| `public bool TryGetOverlay(string id, ref Overlay match)` | 无 | `UnityEditor.EditorWindow` |
| `protected virtual void Finalize()` | 无 | `System.Object` |
| `protected Object MemberwiseClone()` | 无 | `System.Object` |
| `protected virtual void OnBackingScaleFactorChanged()` | 无 | `UnityEditor.EditorWindow` |
| `internal void AddGameTab()` | 无 | `UnityEditor.EditorWindow` |
| `internal void AddSceneTab()` | 无 | `UnityEditor.EditorWindow` |
| `internal virtual bool CanMaximize()` | 无 | `UnityEditor.EditorWindow` |
| `internal void CheckForWindowRepaint()` | 无 | `UnityEditor.EditorWindow` |
| `internal void ClearPersistentViewData()` | 无 | `UnityEditor.EditorWindow` |
| `internal void DisableViewDataPersistence()` | 无 | `UnityEditor.EditorWindow` |
| `internal void DrawNotification()` | 无 | `UnityEditor.EditorWindow` |
| `internal DataModeController GetDataModeController_Internal()` | 无 | `UnityEditor.EditorWindow` |
| `internal Vector2 GetDisplayViewSize(int displayId)` | 无 | `UnityEditor.EditorWindow` |
| `internal GUIContent GetLocalizedTitleContent()` | 无 | `UnityEditor.EditorWindow` |
| `internal int GetNumTabs()` | 无 | `UnityEditor.EditorWindow` |
| `internal ISerializableJsonDictionary GetViewDataDictionary()` | 无 | `UnityEditor.EditorWindow` |
| `internal bool IsSelectedTab()` | 无 | `UnityEditor.EditorWindow` |
| `internal void MakeParentsSettingsMatchMe()` | 无 | `UnityEditor.EditorWindow` |
| `internal void MarkDirty()` | 无 | `UnityEngine.Object` |
| `internal virtual void OnBackgroundViewResized(Rect pos)` | 无 | `UnityEditor.EditorWindow` |
| `internal void OnBackingScaleFactorChangedInternal()` | 无 | `UnityEditor.EditorWindow` |
| `internal virtual void OnMaximized()` | 无 | `UnityEditor.EditorWindow` |
| `internal virtual void OnResized()` | 无 | `UnityEditor.EditorWindow` |
| `internal void ReleaseViewData()` | 无 | `UnityEditor.EditorWindow` |
| `internal void RemoveFromDockArea()` | 无 | `UnityEditor.EditorWindow` |
| `internal void RepaintImmediately()` | 无 | `UnityEditor.EditorWindow` |
| `internal void SaveViewData()` | 无 | `UnityEditor.EditorWindow` |
| `internal void SetDisplayViewSize(int displayId, Vector2 targetSize)` | 无 | `UnityEditor.EditorWindow` |
| `internal void SetMainPlayModeViewSize(Vector2 targetSize)` | 无 | `UnityEditor.EditorWindow` |
| `internal void SetParentGameViewDimensions(Rect rect, Rect clippedRect, Vector2 targetSize)` | 无 | `UnityEditor.EditorWindow` |
| `internal void SetPlayModeView(bool value)` | 无 | `UnityEditor.EditorWindow` |
| `internal void SetPlayModeViewSize(Vector2 targetSize)` | 无 | `UnityEditor.EditorWindow` |
| `internal void ShowAsDropDown(Rect buttonRect, Vector2 windowSize, PopupLocation[] locationPriorityOrder)` | 无 | `UnityEditor.EditorWindow` |
| `internal void ShowAsDropDown(Rect buttonRect, Vector2 windowSize, PopupLocation[] locationPriorityOrder, ShowMode mode)` | 无 | `UnityEditor.EditorWindow` |
| `internal void ShowAsDropDown(Rect buttonRect, Vector2 windowSize, PopupLocation[] locationPriorityOrder, ShowMode mode, bool giveFocus)` | 无 | `UnityEditor.EditorWindow` |
| `internal Rect ShowAsDropDownFitToScreen(Rect buttonRect, Vector2 windowSize, PopupLocation[] locationPriorityOrder)` | 无 | `UnityEditor.EditorWindow` |
| `internal bool ShowNextTabIfPossible()` | 无 | `UnityEditor.EditorWindow` |
| `internal void ShowPopupWithMode(ShowMode mode, bool giveFocus)` | 无 | `UnityEditor.EditorWindow` |
| `internal void ShowTooltip()` | 无 | `UnityEditor.EditorWindow` |
| `internal void ShowWithMode(ShowMode mode)` | 无 | `UnityEditor.EditorWindow` |
| `internal CustomYieldInstruction WaitUntilPresented()` | 无 | `UnityEditor.EditorWindow` |
| `public OdinEditorWindow autoRepaintOnSceneChange { public get; public set; }` | 无 | `UnityEditor.EditorWindow` |
| `public OdinEditorWindow dataModeController { public get; }` | 无 | `UnityEditor.EditorWindow` |
| `public OdinEditorWindow depthBufferBits { public get; public set; }` | 无 | `UnityEditor.EditorWindow` |
| `public OdinEditorWindow docked { public get; }` | 无 | `UnityEditor.EditorWindow` |
| `public OdinEditorWindow hasFocus { public get; }` | 无 | `UnityEditor.EditorWindow` |
| `public OdinEditorWindow hasUnsavedChanges { public get; protected set; }` | 无 | `UnityEditor.EditorWindow` |
| `public OdinEditorWindow hideFlags { public get; public set; }` | 无 | `UnityEngine.Object` |
| `public OdinEditorWindow maxSize { public get; public set; }` | 无 | `UnityEditor.EditorWindow` |
| `public OdinEditorWindow maximized { public get; public set; }` | 无 | `UnityEditor.EditorWindow` |
| `public OdinEditorWindow minSize { public get; public set; }` | 无 | `UnityEditor.EditorWindow` |
| `public OdinEditorWindow name { public get; public set; }` | 无 | `UnityEngine.Object` |
| `public OdinEditorWindow overlayCanvas { public get; }` | 无 | `UnityEditor.EditorWindow` |
| `public OdinEditorWindow position { public get; public set; }` | 无 | `UnityEditor.EditorWindow` |
| `public OdinEditorWindow rootVisualElement { public get; }` | 无 | `UnityEditor.EditorWindow` |
| `public OdinEditorWindow saveChangesMessage { public get; protected set; }` | 无 | `UnityEditor.EditorWindow` |
| `public OdinEditorWindow titleContent { public get; public set; }` | 无 | `UnityEditor.EditorWindow` |
| `public OdinEditorWindow wantsLessLayoutEvents { public get; public set; }` | 无 | `UnityEditor.EditorWindow` |
| `public OdinEditorWindow wantsMouseEnterLeaveWindow { public get; public set; }` | 无 | `UnityEditor.EditorWindow` |
| `public OdinEditorWindow wantsMouseMove { public get; public set; }` | 无 | `UnityEditor.EditorWindow` |
| `internal OdinEditorWindow antiAliasing { internal get; internal set; }` | 无 | `UnityEditor.EditorWindow` |
| `internal OdinEditorWindow baseRootVisualElement { internal get; }` | 无 | `UnityEditor.EditorWindow` |
| `internal OdinEditorWindow disableInputEvents { internal get; internal set; }` | 无 | `UnityEditor.EditorWindow` |
| `internal OdinEditorWindow isUIToolkitWindow { internal get; }` | 无 | `UnityEditor.EditorWindow` |
| `internal OdinEditorWindow liveReloadPreferenceDefault { internal get; }` | 无 | `UnityEditor.EditorWindow` |
| `internal OdinEditorWindow resetPanelRenderingOnAssetChange { internal get; internal set; }` | 无 | `UnityEditor.EditorWindow` |
| `internal OdinEditorWindow viewDataDictionary { internal get; }` | 无 | `UnityEditor.EditorWindow` |
| `internal float m_FadeoutTime` | 无 | `UnityEditor.EditorWindow` |
| `internal bool m_IsPresented` | 无 | `UnityEditor.EditorWindow` |
| `internal GUIContent m_Notification` | 无 | `UnityEditor.EditorWindow` |
| `internal HostView m_Parent` | 无 | `UnityEditor.EditorWindow` |
| `internal Rect m_Pos` | 无 | `UnityEditor.EditorWindow` |
| `internal DataModeController m_SerializedDataModeController` | 无 | `UnityEditor.EditorWindow` |
| `internal GUIContent m_TitleContent` | 无 | `UnityEditor.EditorWindow` |
| `[Obsolete] public void SetDirty()` | 无 | `UnityEngine.ScriptableObject` |
| `[Obsolete] public OdinEditorWindow antiAlias { public get; public set; }` | 无 | `UnityEditor.EditorWindow` |
| `[Obsolete] public OdinEditorWindow title { public get; public set; }` | 无 | `UnityEditor.EditorWindow` |

## Remarks
- Remarks 之后的内容不会被覆盖，可以对特定的方法进行特殊说明
